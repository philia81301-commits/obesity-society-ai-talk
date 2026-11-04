"""把 content/article-hospital-ai-familymed-202611.md 排成院訊投稿 DOCX，右下角放衛教工具集 QR。

QR 以 qrcode 套件從網址重新產生高解析版，內容與入口網站 assets/qr/home.svg 相同。
版面：A4、四邊 2.54cm、12pt 標楷體＋Times New Roman（標楷體 Windows 內建，院方開啟不會跑版）。

用法：python build_hospital_newsletter.py [輸出路徑.docx]
"""
import re
import sys
from pathlib import Path

import qrcode
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.shared import Cm, Pt
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
MD = ROOT.parent / "content" / "article-hospital-ai-familymed-202611.md"
OUT_DIR = ROOT / "hospital-newsletter"
QR_PNG = OUT_DIR / "qr_toolset_with_caption.png"
QR_URL = "https://philia81301-commits.github.io/"
CN_FONT, EN_FONT = "標楷體", "Times New Roman"
QR_WIDTH_CM = 3.2


def build_qr_png():
    """QR 加一行圖說合成一張圖，浮動定位時不會和圖說分家。"""
    OUT_DIR.mkdir(exist_ok=True)
    q = qrcode.QRCode(box_size=30, border=2)  # 預設容錯等級 M，與入口網站原檔相同
    q.add_data(QR_URL)
    q.make(fit=True)
    code = q.make_image(fill_color="black", back_color="white").convert("RGB")
    w, h = code.size
    canvas = Image.new("RGB", (w, h + 110), "white")
    canvas.paste(code, (0, 0))
    draw = ImageDraw.Draw(canvas)
    bold = ImageFont.truetype(r"C:\Windows\Fonts\kaiu.ttf", 100)  # 印出來約 9pt，與內文同為標楷體
    draw.text((w / 2, h - 10), "掃描開啟衛教工具集", fill="#222222", font=bold, anchor="ma")
    canvas.save(QR_PNG, dpi=(600, 600))
    return canvas.size


def style_run(run, size=12, bold=False):
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.name = EN_FONT
    run._element.rPr.rFonts.set(qn("w:eastAsia"), CN_FONT)


def float_bottom_right(run, width_cm, size):
    """把行內圖改成錨定在版心右下角、文繞圖的浮動圖。"""
    run.add_picture(str(QR_PNG), width=Cm(width_cm))
    inline = run._element.xpath(".//wp:inline")[0]
    cx, cy = int(inline.extent.cx), int(inline.extent.cy)
    graphic = inline.xpath("./a:graphic")[0]
    doc_pr = inline.xpath("./wp:docPr")[0]
    doc_pr.set("descr", "掃描開啟衛教工具集 QR code")
    anchor = parse_xml(
        f'<wp:anchor {nsdecls("wp", "a")} distT="0" distB="0" distL="144000" distR="0" simplePos="0" '
        f'relativeHeight="2" behindDoc="0" locked="0" layoutInCell="1" allowOverlap="0">'
        f'<wp:simplePos x="0" y="0"/>'
        f'<wp:positionH relativeFrom="margin"><wp:align>right</wp:align></wp:positionH>'
        f'<wp:positionV relativeFrom="margin"><wp:align>bottom</wp:align></wp:positionV>'
        f'<wp:extent cx="{cx}" cy="{cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/>'
        f'<wp:wrapSquare wrapText="left"/>'
        f'<wp:docPr id="{doc_pr.get("id")}" name="QR" descr="{doc_pr.get("descr")}"/>'
        f'<wp:cNvGraphicFramePr/></wp:anchor>'
    )
    anchor.append(graphic)
    inline.getparent().replace(inline, anchor)


def body_lines():
    text = re.sub(r"<!--[\s\S]*?-->", "", MD.read_text(encoding="utf-8"))
    return [ln.strip() for ln in text.splitlines() if ln.strip()]


def build(out):
    size = build_qr_png()
    doc = Document()
    s = doc.sections[0]
    s.page_width, s.page_height = Cm(21), Cm(29.7)
    s.top_margin = s.bottom_margin = Cm(2.54)
    s.left_margin = s.right_margin = Cm(2.54)  # 比學會體例略窄，讓全文收在一頁

    lines = body_lines()
    first = True
    for ln in lines:
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.line_spacing = 1.05
        pf.space_after = Pt(5)
        if ln.startswith("# "):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            style_run(p.add_run(ln[2:]), size=16, bold=True)
            pf.space_after = Pt(4)
        elif ln.startswith("## "):
            style_run(p.add_run(ln[3:]), size=13, bold=True)
            pf.space_before = Pt(7)
            pf.space_after = Pt(3)
            pf.keep_with_next = True
        elif ln.startswith("家庭醫學部"):
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            style_run(p.add_run(ln), size=11)
            pf.space_after = Pt(6)
        else:
            if first:  # 浮動圖錨在第一段內文，定位以版心為準
                float_bottom_right(p.add_run(), QR_WIDTH_CM, size)
                first = False
            style_run(p.add_run(ln))
    doc.save(out)


def count_chars():
    lines = body_lines()
    body = [l for l in lines if not l.startswith("# ") and not l.startswith("家庭醫學部") and not l.startswith("## ")]
    joined = "".join(body)
    heads = "".join(l[3:] for l in lines if l.startswith("## "))
    print("內文字數（含標點）：", len(re.sub(r"\s", "", joined)))
    print("含小標字數：", len(re.sub(r"\s", "", joined + heads)))


if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else OUT_DIR / "院訊_AI在家庭醫學科的應用_潘湘如_20261104.docx"
    OUT_DIR.mkdir(exist_ok=True)
    build(out)
    count_chars()
    print("已輸出", out)
