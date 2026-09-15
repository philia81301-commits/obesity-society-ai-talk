"""把離線 HTML 簡報轉成「可編輯」PPTX（2026-09-15 起的新做法）。

與 build_pptx.py（整頁截圖＋備忘稿）的差別：
  * 每頁仍以 Playwright 截圖當**投影片背景**（保留 SVG 圖標、CSS 圖表、底圖、色塊、分隔線），
    但截圖前先把所有文字設成透明，所以底圖裡**沒有字**。
  * 文字改由 python-pptx 依 DOM 量到的位置、字級、粗細、顏色、行高，逐段放成原生文字方塊，
    疊在底圖正確位置。使用者在 PowerPoint 裡改字、改字級、搬位置都會直接呈現。
  * 底圖走 <p:bg> 投影片背景而不是圖片物件：編輯時點不到、拖不動，不會誤移。
  * SVG 內的文字（圖表軸標、圖標上的字）與 Reveal 右下頁碼仍在底圖裡，不可編輯——
    這類文字很少，且與版面圖形綁死，重畫反而失真。

為什麼不整份重畫成原生元件：HTML 是母本，圖形類元素（漸層遮罩、手繪底圖、CSS 堆疊圖）
原生 PPTX 畫不出一致效果；「底圖＋文字方塊」是保真與可編輯之間的折衷。

字型：
  * 內文 'Noto Sans TC'（這台機器 C:\\Windows\\Fonts 已裝 NotoSansTC-VF.ttf）。
  * 標題 'Noto Serif TC' 若機器沒裝，PowerPoint 會用新細明體替代，很醜；
    腳本會檢查登錄檔，沒裝就退回 Noto Sans TC，並印出提示。可用環境變數覆寫：
      FONT_HEAD="Noto Serif TC"  FONT_BODY="Noto Sans TC"

用法：python build_pptx_editable.py <輸出.pptx>
需先啟動本機伺服器（repo 根目錄 python -m http.server 8770），並確認 URL 指到本專案。
"""

import os
import re
import sys
import time
import winreg
from pathlib import Path

from lxml import etree
from playwright.sync_api import sync_playwright
from pptx import Presentation
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Pt

URL = os.environ.get("SLIDES_URL", "http://127.0.0.1:8770/slides/index.html")
W, H = 1280, 720
SCALE = 2                      # 底圖 2560x1440
EMU_PER_PX = 9525              # 13.333in × 914400 / 1280px
PT_PER_PX = 0.75
SHOTS = Path("shots_editable")

# 文字框比量到的寬度多留一點，避免 PowerPoint 字距略寬時多折一行
WIDTH_SLACK = 0.03
# PowerPoint「固定行距」時字面在行框內的落點與瀏覽器略有差異，實測校正（px，正值往下）
TOP_NUDGE_PX = float(os.environ.get("TOP_NUDGE_PX", "0"))


def installed_font(name: str) -> bool:
    for root in (winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER):
        try:
            k = winreg.OpenKey(root, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts")
        except OSError:
            continue
        i = 0
        while True:
            try:
                v, _, _ = winreg.EnumValue(k, i)
            except OSError:
                break
            if name.lower() in v.lower():
                return True
            i += 1
    return False


# 兩套字型都會嵌進 PPTX（見 pptx_fonts.py），所以不必看機器有沒有裝；環境變數仍可覆寫
FONT_BODY = os.environ.get("FONT_BODY", "Noto Sans TC")
FONT_HEAD = os.environ.get("FONT_HEAD", "Noto Serif TC")
FONT_MAP = {"Noto Sans TC": FONT_BODY, "Noto Serif TC": FONT_HEAD}
EMBED_FONTS = os.environ.get("EMBED_FONTS", "1") == "1"


# ---------------------------------------------------------------------------
# 瀏覽器端：把目前頁的文字拆成「段落方塊」並回傳幾何與樣式
# ---------------------------------------------------------------------------
COLLECT_JS = r"""
(idx) => {
  const sec = document.querySelectorAll('.slides > section')[idx];
  const scale = document.querySelector('.slides').getBoundingClientRect().width / 1280;
  const INLINE = new Set(['inline', 'inline-block', 'inline-flex', 'inline-grid', 'contents']);
  const CJK = /[\u2E80-\u9FFF\uF900-\uFAFF\uFF00-\uFFEF]/;
  const blocks = [];
  const hideEls = [];

  const cs = (el) => getComputedStyle(el);
  const isSvg = (el) => el.namespaceURI === 'http://www.w3.org/2000/svg';
  function shown(el) {
    const s = cs(el);
    if (s.display === 'none' || s.visibility === 'hidden') return false;
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0;
  }
  function effOpacity(el) {
    let o = 1;
    for (let e = el; e && e !== sec.parentElement; e = e.parentElement) o *= parseFloat(cs(e).opacity);
    return o;
  }
  function hasBlockDesc(el) {
    for (const d of el.querySelectorAll('*')) {
      if (isSvg(d)) continue;
      const s = cs(d);
      if (s.display === 'none') continue;
      if (!INLINE.has(s.display)) return true;
    }
    return false;
  }
  function textOf(el) { return (el.innerText || '').trim(); }

  function normWS(s) {
    // 段落內原始碼換行先標成 \u0001，稍後看兩側是否皆 CJK 決定刪除或轉空白（Blink 行為）
    return s.replace(/[ \t\r\f]*\n[ \t\r\f]*/g, '\u0001').replace(/[ \t\r\f]+/g, ' ');
  }

  // 「標籤」：有左右 padding 或邊框的 inline-block（如 .caveat、.kicker），字面位置受 padding 影響，
  // 必須獨立成自己的文字方塊，不能併進所在段落。
  function isChip(el) {
    const s = cs(el);
    if (s.display !== 'inline-block' && s.display !== 'inline-flex') return false;
    return parseFloat(s.paddingLeft) + parseFloat(s.paddingRight) +
           parseFloat(s.borderLeftWidth) + parseFloat(s.borderRightWidth) > 0;
  }

  function runsOfNodes(nodes) {
    const runs = [];
    for (const root of nodes) {
      if (root.nodeType === 3) { pushText(root); continue; }
      const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT | NodeFilter.SHOW_ELEMENT, {
        acceptNode(n) {
          if (n.nodeType === 1) {
            if (isSvg(n)) return NodeFilter.FILTER_REJECT;
            const s = cs(n);
            if (s.display === 'none' || s.visibility === 'hidden') return NodeFilter.FILTER_REJECT;
            return n.tagName === 'BR' ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP;
          }
          return n.data.length ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
        }
      });
      if (root.nodeType === 1 && root.tagName === 'BR') { runs.push({ text: '\n' }); continue; }
      let n;
      while ((n = walker.nextNode())) {
        if (n.nodeType === 1) { runs.push({ text: '\n' }); continue; }
        pushText(n);
      }
    }
    function pushText(n) {
      const p = n.parentElement;
      const s = cs(p);
      let t = normWS(n.data);
      if (s.textTransform === 'uppercase') t = t.toUpperCase();
      else if (s.textTransform === 'lowercase') t = t.toLowerCase();
      runs.push({
        text: t,
        size: parseFloat(s.fontSize) * scale,
        weight: parseInt(s.fontWeight, 10) || 400,
        italic: s.fontStyle !== 'normal',
        color: s.color,
        family: s.fontFamily,
        underline: s.textDecorationLine.includes('underline'),
        letterSpacing: s.letterSpacing === 'normal' ? 0 : parseFloat(s.letterSpacing) * scale,
        opacity: effOpacity(p),
        shadow: s.textShadow === 'none' ? '' : s.textShadow,
      });
    }
    const out = runs;
    const lastCharBefore = (i, res) => {
      let before = res.replace(/[\s\u0001]+$/, '').slice(-1);
      for (let j = i - 1; j >= 0 && !before; j--) before = out[j].text === '\n' ? '\n' : out[j].text.replace(/[\s\u0001]+$/, '').slice(-1);
      return before;
    };
    const firstCharAfter = (i, rest) => {
      let after = rest.replace(/^[\s\u0001]+/, '').slice(0, 1);
      for (let j = i + 1; j < out.length && !after; j++) after = out[j].text === '\n' ? '\n' : out[j].text.replace(/^[\s\u0001]+/, '').slice(0, 1);
      return after;
    };
    for (let i = 0; i < out.length; i++) {
      const r = out[i];
      if (r.text === '\n') continue;
      let res = '';
      for (let k = 0; k < r.text.length; k++) {
        const ch = r.text[k];
        if (ch !== '\u0001') { res += ch; continue; }
        const before = lastCharBefore(i, res);
        const after = firstCharAfter(i, r.text.slice(k + 1));
        if (CJK.test(before) && CJK.test(after)) continue;
        res += ' ';
      }
      r.text = res.replace(/ {2,}/g, ' ');
    }
    // 去段首／段尾／換行兩側空白；空 run 丟掉
    for (let i = 0; i < out.length; i++) {
      const r = out[i];
      if (r.text === '\n') continue;
      const atStart = i === 0 || out[i - 1].text === '\n';
      const atEnd = i === out.length - 1 || out[i + 1].text === '\n';
      if (atStart) r.text = r.text.replace(/^\s+/, '');
      if (atEnd) r.text = r.text.replace(/\s+$/, '');
    }
    const kept = out.filter(r => r.text !== '');
    while (kept.length && kept[0].text === '\n') kept.shift();
    while (kept.length && kept[kept.length - 1].text === '\n') kept.pop();
    return kept;
  }

  // 依「行高」分行：大字的字面（內容區）常比行高還高，上下行會互相重疊，
  // 不能用「矩形是否重疊」判斷（2026-09-15 封面標題兩行被併成一行、整體下移 50px 的教訓）
  function lineRects(rangeRects, lh) {
    const rs = [...rangeRects].filter(r => r.width > 0 && r.height > 0).sort((a, b) => a.top - b.top);
    const lines = [];
    for (const r of rs) {
      const L = lines[lines.length - 1];
      if (L && r.top < L.top + lh * 0.5) { L.top = Math.min(L.top, r.top); L.bottom = Math.max(L.bottom, r.bottom); }
      else lines.push({ top: r.top, bottom: r.bottom });
    }
    return lines;
  }

  function rangeOf(nodes) {
    const rg = document.createRange();
    rg.setStartBefore(nodes[0]);
    rg.setEndAfter(nodes[nodes.length - 1]);
    return rg;
  }

  // el：提供樣式（行高、對齊、內容框）的元素；nodes：實際要收的節點（預設 el 的全部子節點）
  function pushBlock(el, nodes, opts = {}) {
    const s = cs(el);
    nodes = nodes || [...el.childNodes];
    if (!nodes.length) return;
    const rr = [...rangeOf(nodes).getClientRects()].filter(x => x.width > 0 && x.height > 0);
    if (!rr.length) return;
    const fs = parseFloat(s.fontSize) * scale;
    const lh = s.lineHeight === 'normal' ? rr[0].height : parseFloat(s.lineHeight) * scale;
    const lines = lineRects(rr, lh);
    const runs = runsOfNodes(nodes);
    if (!runs.length) return;
    const r = el.getBoundingClientRect();
    const padL = parseFloat(s.paddingLeft) * scale, padR = parseFloat(s.paddingRight) * scale;
    const bL = parseFloat(s.borderLeftWidth) * scale, bR = parseFloat(s.borderRightWidth) * scale;
    const textL = Math.min(...rr.map(x => x.left)), textR = Math.max(...rr.map(x => x.right));
    let left, width;
    const align = s.textAlign;
    if (opts.tight || s.display === 'inline' || s.display === 'contents') {
      left = textL; width = textR - left;
    } else if (align === 'center' || align === 'right' || align === 'end') {
      left = r.left + bL + padL; width = r.width - bL - bR - padL - padR;
    } else {
      // 靠左：起點用實際字面（跳過 ::before 之類的行內裝飾），右界用內容框
      left = textL; width = (r.right - bR - padR) - left;
    }
    const glyphH = lines[0].bottom - lines[0].top;
    const halfLead = (lh - glyphH) / 2;
    const top = lines[0].top - halfLead;
    const height = Math.max(lh * lines.length, lines[lines.length - 1].bottom + halfLead - top);
    blocks.push({
      left, top, width, height, lines: lines.length,
      align, lineHeight: lh, fontSize: fs, runs,
      tag: el.tagName.toLowerCase(),
    });
  }

  // 葉節點（沒有區塊型子孫）：以標籤為界切段，其餘節點併成同一段落
  function pushLeaf(el) {
    const kids = [...el.childNodes];
    let seg = [];
    const flush = () => { if (seg.some(n => (n.textContent || '').trim())) pushBlock(el, seg, { tight: seg.length !== kids.length }); seg = []; };
    for (const n of kids) {
      if (n.nodeType === 1 && isChip(n)) { flush(); pushBlock(n); }
      else seg.push(n);
    }
    flush();
    hideEls.push(el);
  }

  function walk(el) {
    if (isSvg(el) || !shown(el)) return;
    if (!textOf(el)) return;
    if (!hasBlockDesc(el)) { pushLeaf(el); return; }
    for (const n of [...el.childNodes]) {
      if (n.nodeType === 3) {
        if (!n.data.trim()) continue;
        const span = document.createElement('span');
        span.className = 'pptx-wrap';
        n.parentNode.insertBefore(span, n); span.appendChild(n);
        pushBlock(span, [n], { tight: true });
        hideEls.push(span);
      } else if (n.nodeType === 1) {
        walk(n);
      }
    }
  }
  walk(sec);
  for (const e of hideEls) e.classList.add('pptx-hide');
  return { scale, blocks };
}
"""

UNHIDE_JS = r"""
() => {
  document.querySelectorAll('.pptx-hide').forEach(e => e.classList.remove('pptx-hide'));
  document.querySelectorAll('span.pptx-wrap').forEach(s => { s.replaceWith(...s.childNodes); });
}
"""


def render(only: set[int] | None = None) -> list[dict]:
    SHOTS.mkdir(exist_ok=True)
    out = []
    with sync_playwright() as pw:
        try:
            browser = pw.chromium.launch(channel="chrome")
        except Exception:
            browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": W, "height": H}, device_scale_factor=SCALE)
        # ⚠️ 不可用 networkidle（Firebase 長連線）
        page.goto(URL, wait_until="load")
        page.wait_for_function("typeof Reveal !== 'undefined' && Reveal.isReady()")
        page.add_style_tag(content="""
            .reveal .controls, .reveal .progress { display:none !important; }
            .pptx-hide, .pptx-hide * {
              color: transparent !important;
              -webkit-text-fill-color: transparent !important;
              text-shadow: none !important;
              text-decoration-color: transparent !important;
            }
        """)
        page.evaluate("document.fonts.ready")
        time.sleep(1.2)
        total = page.evaluate("document.querySelectorAll('.slides > section').length")
        print(f"共 {total} 頁，開始擷取…")
        for i in range(total):
            if only and (i + 1) not in only:
                continue
            page.evaluate(f"Reveal.slide({i})")
            time.sleep(0.45)
            text = page.evaluate(f"document.querySelectorAll('.slides > section')[{i}].innerText")
            info = page.evaluate(COLLECT_JS, i)
            time.sleep(0.05)
            f = SHOTS / f"slide_{i + 1:02d}.png"
            page.screenshot(path=str(f))
            page.evaluate(UNHIDE_JS)
            out.append({"img": f, "text": (text or "").strip(), "num": i + 1, **info})
            if (i + 1) % 10 == 0:
                print(f"  已完成 {i + 1}/{total}")
        browser.close()
    return out


# ---------------------------------------------------------------------------
# python-pptx 端
# ---------------------------------------------------------------------------
def parse_color(c: str):
    """rgb()/rgba()，以及 color-mix() 算出來的 color(srgb r g b / a)（0–1 浮點）。"""
    m = re.match(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", c)
    if m:
        r, g, b = (int(round(float(m.group(k)))) for k in (1, 2, 3))
        a = float(m.group(4)) if m.group(4) is not None else 1.0
        return (r, g, b), a
    m = re.match(r"color\(srgb\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)(?:\s*/\s*([\d.]+))?\)", c)
    if m:
        r, g, b = (int(round(float(m.group(k)) * 255)) for k in (1, 2, 3))
        a = float(m.group(4)) if m.group(4) is not None else 1.0
        return (max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b))), a
    print(f"  ⚠️ 無法解析顏色：{c}")
    return (0, 0, 0), 1.0


def parse_shadow(sh: str):
    """取 text-shadow 裡位移最大的那一層，回傳 (rgb, alpha, dx, dy, blur)；用來近似封面立體字。"""
    best = None
    for part in re.findall(r"(rgba?\([^)]*\)|color\([^)]*\))\s+(-?[\d.]+)px\s+(-?[\d.]+)px(?:\s+(-?[\d.]+)px)?", sh):
        (rgb, a), dx, dy = parse_color(part[0]), float(part[1]), float(part[2])
        blur = float(part[3] or 0)
        if blur > 0:
            continue                      # 柔影另計，這裡只要「厚度」
        if best is None or abs(dx) + abs(dy) > abs(best[2]) + abs(best[3]):
            best = (rgb, a, dx, dy, blur)
    return best


def add_shadow(rPr, shadow: str, scale: float):
    best = parse_shadow(shadow)
    if not best:
        return
    (cr, cg, cb), a, dx, dy, _ = best
    import math
    dist = math.hypot(dx, dy) * scale * EMU_PER_PX
    ang = int(round(math.degrees(math.atan2(dy, dx)) % 360 * 60000))
    eff = etree.Element(qn("a:effectLst"))
    rPr.insert(1, eff)                        # 緊接 solidFill 之後、latin 之前
    sh = etree.SubElement(eff, qn("a:outerShdw"), blurRad="0", dist=str(int(dist)), dir=str(ang),
                          algn="tl", rotWithShape="0")
    clr = etree.SubElement(sh, qn("a:srgbClr"), val=f"{cr:02X}{cg:02X}{cb:02X}")
    if a < 0.995:
        etree.SubElement(clr, qn("a:alpha"), val=str(int(round(a * 100000))))


def family_of(ff: str) -> str:
    first = ff.split(",")[0].strip().strip('"').strip("'")
    return FONT_MAP.get(first, first)


ALIGN = {"center": PP_ALIGN.CENTER, "right": PP_ALIGN.RIGHT, "end": PP_ALIGN.RIGHT,
         "justify": PP_ALIGN.JUSTIFY}


def set_background(slide, img: Path):
    """把截圖設成投影片背景（不可選取的 <p:bg>）。"""
    _, rId = slide.part.get_or_add_image_part(str(img))
    cSld = slide._element.find(qn("p:cSld"))
    for old in cSld.findall(qn("p:bg")):
        cSld.remove(old)
    bg = etree.Element(qn("p:bg"))
    cSld.insert(0, bg)
    bgPr = etree.SubElement(bg, qn("p:bgPr"))
    blip = etree.SubElement(bgPr, qn("a:blipFill"), dpi="0", rotWithShape="1")
    etree.SubElement(blip, qn("a:blip"), {qn("r:embed"): rId})
    st = etree.SubElement(blip, qn("a:stretch"))
    etree.SubElement(st, qn("a:fillRect"))
    etree.SubElement(bgPr, qn("a:effectLst"))


def add_run(p, run: dict, scale: float = 1.0):
    r = p.add_run()
    r.text = run["text"]
    f = r.font
    f.size = Pt(run["size"] * PT_PER_PX)
    f.italic = bool(run["italic"])
    if run["underline"]:
        f.underline = True
    fam = family_of(run["family"])
    if run["weight"] >= 850 and EMBED_FONTS and fam in ("Noto Sans TC", "Noto Serif TC"):
        fam += " Black"                       # 900 另立家族（PowerPoint 只認 Regular/Bold）
        f.bold = False
    else:
        f.bold = run["weight"] >= 600
    f.name = fam                              # <a:latin>
    rPr = r._r.get_or_add_rPr()
    ea = rPr.find(qn("a:ea"))
    if ea is None:
        ea = etree.SubElement(rPr, qn("a:ea"))  # 中文走 <a:ea>，不設會退回佈景主題的新細明體
    ea.set("typeface", fam)
    (cr, cg, cb), a = parse_color(run["color"])
    a *= run.get("opacity", 1.0)
    solid = etree.Element(qn("a:solidFill"))
    clr = etree.SubElement(solid, qn("a:srgbClr"), val=f"{cr:02X}{cg:02X}{cb:02X}")
    if a < 0.995:
        etree.SubElement(clr, qn("a:alpha"), val=str(int(round(a * 100000))))
    rPr.insert(0, solid)                      # schema 順序：solidFill → effectLst → latin/ea
    if run.get("shadow"):
        add_shadow(rPr, run["shadow"], scale)
    if run["letterSpacing"]:
        rPr.set("spc", str(int(round(run["letterSpacing"] * PT_PER_PX * 100))))


def build(slides: list[dict], dest: Path) -> int:
    prs = Presentation()
    prs.slide_width = Emu(W * EMU_PER_PX)
    prs.slide_height = Emu(H * EMU_PER_PX)
    blank = prs.slide_layouts[6]
    n_boxes = 0
    for s in slides:
        slide = prs.slides.add_slide(blank)
        set_background(slide, s["img"])
        for b in s["blocks"]:
            align = ALIGN.get(b["align"], PP_ALIGN.LEFT)
            left, width = b["left"], b["width"]
            slack = width * WIDTH_SLACK
            if align == PP_ALIGN.CENTER:
                left -= slack / 2
                width += slack
            elif align == PP_ALIGN.RIGHT:
                left -= slack
                width += slack
            else:
                width += slack
            top = b["top"] + TOP_NUDGE_PX * (b["fontSize"] / 26.7)
            box = slide.shapes.add_textbox(Emu(int(left * EMU_PER_PX)), Emu(int(top * EMU_PER_PX)),
                                           Emu(int(width * EMU_PER_PX)), Emu(int(b["height"] * EMU_PER_PX)))
            first = b["runs"][0]["text"][:20].replace("\n", " ")
            box.name = f"P{s['num']} {b['tag']} {first}"
            tf = box.text_frame
            tf.word_wrap = True
            tf.auto_size = MSO_AUTO_SIZE.NONE
            tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
            tf.vertical_anchor = MSO_ANCHOR.TOP
            p = tf.paragraphs[0]
            p.alignment = align
            p.line_spacing = Pt(b["lineHeight"] * PT_PER_PX)
            for run in b["runs"]:
                if run["text"] == "\n":
                    p._p.add_br()
                    continue
                add_run(p, run, s["scale"])
            n_boxes += 1
        if s["text"]:
            slide.notes_slide.notes_text_frame.text = s["text"]
    if EMBED_FONTS:
        from pptx_fonts import embed_fonts
        print("嵌入字型：" + "／".join(embed_fonts(prs)))
    dest.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(dest))
    return n_boxes


def main():
    if len(sys.argv) < 2:
        sys.exit("用法：python build_pptx_editable.py <輸出.pptx> [只做這些頁，如 1,2,10]")
    dest = Path(sys.argv[1])
    only = {int(x) for x in sys.argv[2].split(",")} if len(sys.argv) > 2 else None
    print(f"字型：內文 {FONT_BODY}／標題 {FONT_HEAD}（{'嵌入 PPTX' if EMBED_FONTS else '不嵌入，依機器安裝狀況'}）")
    slides = render(only)
    n = build(slides, dest)
    mb = dest.stat().st_size / 1024 / 1024
    print(f"\n已輸出：{dest}\n頁數：{len(slides)}　文字方塊：{n}　檔案大小：{mb:.1f} MB")


if __name__ == "__main__":
    main()
