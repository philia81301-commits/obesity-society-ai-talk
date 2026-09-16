"""依 slides/index.html（51 頁定版）產出一頁 A4 演講摘要 DOCX。

版面沿用 article/build_docx.py 的字型體例（中文新細明體、英文 Calibri），
但為了塞進一頁，左右邊界 1.9cm、上下 1.4／1.2cm、內文 10.5pt、行距 1.12–1.2。
段落標題色 #1B4332 與簡報 --accent 一致。

用法：python build_summary_docx.py [輸出路徑.docx]
內容有異動時直接改本檔的 CONTENT 區塊後重跑。
"""
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

CN_FONT = "新細明體"
EN_FONT = "Calibri"
ACCENT = RGBColor(0x1B, 0x43, 0x32)
GREY = RGBColor(0x55, 0x55, 0x55)
BODY = 10.5

DEFAULT_OUT = Path(
    r"C:\Users\phili\OneDrive\文件\演講\2026演講\肥胖醫學會南區研討會"
    r"\肥胖醫學會南區研討會_AI在肥胖治療_一頁摘要_潘湘如_20260913.docx"
)

# ---------- 內容（依 51 頁定版整理） ----------

TITLE = "人工智慧在肥胖治療運用的新發展"
SUBTITLE = "演講摘要｜台灣肥胖醫學會 2026 南區學術研討會｜2026 年 9 月 20 日"
SPEAKER = "潘湘如 醫師｜高雄榮民總醫院 家庭醫學部"

ABSTRACT = (
    "減重的真正難題不在減下來，而在維持：減重後 2 年內逾半數、5 年內逾八成復胖；"
    "門診端又受行政負擔重、衛教時間不足、專科可近性有限等結構性限制。"
    "AI 技術的快速演進正與此需求交會。本演講以「發展脈絡 → 現況實務 → 落地挑戰」三段架構，"
    "回顧 AI 在肥胖醫學的應用演進，並以講者自行開發、目前提供院內使用的減重門診工具為案例，"
    "說明臨床導入的實際樣貌，以及必須同步守住的資安與個資界線。"
)

SECTIONS = [
    (
        "Ⅰ　發展脈絡：AI 在肥胖醫學運用的過去與現在（2018–2026）",
        [
            "**奠基期 2018–2022，證明「可預測」**：學齡前兒童肥胖風險模型（GBM，n=9,478）指出進食速度、含糖飲料等可介入因子；"
            "非監督式分群顯示肥胖者逾半數帶有代謝異常——BMI 相同，風險未必相同。",
            "**驗證期 2022–2024，證明「有效果」**：穿戴裝置與數位行為介入的統合分析顯示每日步數 +1,800、步行 +40 分鐘，"
            "但體重僅減約 1 公斤；單靠監測不足以處理肥胖，必須與臨床介入結合。COVID-19 意外成為遠距減重的大規模自然實驗。",
            "**精準醫療期 2025–2026，證明「可決策」**：基因風險分數預測 liraglutide 噁心副作用（68% vs 30%，n=110，會議摘要層級）；"
            "TiP DecScore 於 <55 歲亞組中，用藥符合 AI 建議者 HbA1c 控制率 64.1% vs 46.2%。重點不是讓藥更有效，而是用 AI 挑對病人、配置有限的藥物資源。",
            "**政策已到位，指引證據等級還沒跟上**：台灣《成人肥胖指引 2025》將 AI 聊天機器人與 CDSS 列為 2C（醫療科技介入整體 1A）；"
            "ADA 2026 肥胖章節全章未提 AI，遠距／app 僅 E 級。缺的是可納入系統性回顧的實務證據。",
        ],
    ),
    (
        "Ⅱ　現況實務：減重門診生態系為主線，其餘門診工具為輔線",
        [
            "**案例 01 減重評估表單**（不含 AI 技術，由 AI agent 輔助開發、當天上線）：病人初診前線上自填＋醫師看診時下拉選單輸入，"
            "寫入同一份試算表；一鍵產生病歷貼稿。這是下游兩個 AI 應用共同的資料基礎建設。",
            "**案例 02 門診 AI 管理系統（RAG）**：以院內既有衛教單張與治療指引為知識庫，生成限制在檢索內容之內並附出處，以降低幻覺；"
            "敏感議題不由模型作答、轉介真人——臨床判斷不外包給 AI。",
            "**案例 03 月度分析自動化**（18 天上線）：每月自動產出新增個案特徵、藥物別成效、未回診率報告並發布雲端；"
            "衍生「減重大冒險」衛教遊戲，推薦數字隨月報同步更新，n<10 組別不列入比較。",
            "**輔線**：骨鬆風險評估（跨一夜）、肌少症篩檢（13 分鐘，PWA 離線）、HP-clinic、pneumonia-clinic，"
            "皆為純前端、不存個資、地端運算。共通方法論：需求盤點 → 最小可行版本 → 迭代驗證。",
        ],
    ),
    (
        "Ⅲ　落地挑戰：資訊安全與個資保護",
        [
            "**兩道法規界線**：個資法第 6 條——病歷等特種個資原則禁止利用，去識別化是法定入場券；"
            "AI 非法律主體，診斷與處方責任仍在醫師；以 LINE 等對外發布的 AI 回覆可能被認定為醫療廣告，不得誇大療效。",
            "**去識別化不等於安全**：Strava 熱圖反推軍事基地、Netflix 匿名評分 99% 還原身分、郵遞區號＋生日＋性別定位 87% 美國人——"
            "少數欄位的組合即成指紋，這正是月報一律聚合呈現的理由。",
            "**生成式 AI 風險矩陣**：語音 AI（錄音外洩、轉錄錯誤）、病歷摘要（未經確認即進病歷）、問答機器人（Prompt Injection）；"
            "共通風險為資料串聯、跨境傳輸與模型訓練的二次利用。",
            "**主張**：「資料不上傳」是比「去識別化」更上游的防線；資安治理應內建於工具設計階段，而非事後補救。",
        ],
    ),
]

CLOSING_HEAD = "結語：給想從自己門診開始的臨床工作者"
CLOSING = (
    "從最耗時的例行工作開始，而不是從最新的技術開始；先做最小可行版本，讓它在真實門診跑一週再決定要不要長大；"
    "資料設計比功能設計更重要，結構化的一次輸入能餵養後續所有應用；資安從第一天內建，能不上傳的資料就不要上傳。"
    "**AI 提供地圖，醫師擔任嚮導**——人力有限的門診尤其如此，AI 補上的是原本就空著的位置。"
)

FOOTNOTE = (
    "第Ⅲ段個資論述主要資料來源：成功大學計算機與網路中心 李南逸主任《AI 時代之醫療隱私與個資保護挑戰》講義；"
    "責任歸屬與醫療廣告部分依醫師法、醫療法。文獻出處詳見簡報各頁。"
)


# ---------- 排版工具 ----------

def set_run(run, *, size=BODY, bold=False, color=None):
    run.font.size = Pt(size)
    run.font.name = EN_FONT
    run.font.bold = bold
    if color is not None:
        run.font.color.rgb = color
    run._element.rPr.rFonts.set(qn("w:eastAsia"), CN_FONT)


def add_rich(p, text, *, size=BODY, color=None):
    """處理 **粗體**。"""
    parts = text.split("**")
    for i, part in enumerate(parts):
        if part:
            set_run(p.add_run(part), size=size, bold=(i % 2 == 1), color=color)


def para(doc, text="", *, size=BODY, align=None, before=0, after=3, line=1.15,
         color=None, bold=False):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = line
    if align is not None:
        p.alignment = align
    if text:
        if bold:
            set_run(p.add_run(text), size=size, bold=True, color=color)
        else:
            add_rich(p, text, size=size, color=color)
    return p


def bottom_border(p, color="1B4332", sz=8):
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    b = OxmlElement("w:bottom")
    b.set(qn("w:val"), "single")
    b.set(qn("w:sz"), str(sz))
    b.set(qn("w:space"), "1")
    b.set(qn("w:color"), color)
    pbdr.append(b)
    pPr.append(pbdr)


def heading(doc, text):
    p = para(doc, before=5, after=2, line=1.1)
    set_run(p.add_run(text), size=11.5, bold=True, color=ACCENT)
    p.paragraph_format.keep_with_next = True
    bottom_border(p, sz=6)
    return p


def bullet(doc, text):
    p = doc.add_paragraph(style="List Bullet")
    pf = p.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(2)
    pf.line_spacing = 1.12
    # 懸掛縮排：換行後對齊項目文字而非符號（覆寫 List Bullet 樣式的縮排＋補 tab stop）
    pf.left_indent = Cm(0.55)
    pf.first_line_indent = Cm(-0.55)
    pf.tab_stops.add_tab_stop(Cm(0.55))
    add_rich(p, text)
    return p


# ---------- 主流程 ----------

def build(dest: Path):
    doc = Document()
    st = doc.styles["Normal"]
    st.font.name = EN_FONT
    st.font.size = Pt(BODY)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), CN_FONT)

    s = doc.sections[0]
    s.page_width, s.page_height = Cm(21.0), Cm(29.7)
    s.left_margin = s.right_margin = Cm(1.9)
    s.top_margin = Cm(1.4)
    s.bottom_margin = Cm(1.2)

    # 標題區
    p = para(doc, after=1, line=1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_run(p.add_run(TITLE), size=18, bold=True, color=ACCENT)
    para(doc, SUBTITLE, size=10, after=0, line=1.0, align=WD_ALIGN_PARAGRAPH.CENTER, color=GREY)
    p = para(doc, SPEAKER, size=10, after=4, line=1.0, align=WD_ALIGN_PARAGRAPH.CENTER, color=GREY)
    bottom_border(p, sz=12)

    # 摘要
    p = para(doc, before=4, after=4, line=1.2)
    set_run(p.add_run("摘要　"), bold=True, color=ACCENT)
    add_rich(p, ABSTRACT)

    for head, items in SECTIONS:
        heading(doc, head)
        for it in items:
            bullet(doc, it)

    heading(doc, CLOSING_HEAD)
    para(doc, CLOSING, before=1, after=4, line=1.2)

    p = para(doc, FOOTNOTE, size=8.5, before=4, after=0, line=1.1, color=GREY)

    dest.parent.mkdir(parents=True, exist_ok=True)
    doc.save(dest)
    print("saved:", dest)


if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT
    build(out)
