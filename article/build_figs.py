"""產生會訊專論用的圖一（流程示意）與圖四（門診三步驟組圖）。

圖一：以 Playwright 截取 fig1_flow.html（2 倍解析度，印刷用）。
圖四：把三張已去識別化的門診實拍等高併成橫幅，加上步驟標籤。
輸出至 article/figs/。
"""
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "figs"
OUT.mkdir(exist_ok=True)
IMG = ROOT.parent / "slides" / "images"

FONT = r"C:\Windows\Fonts\msjhbd.ttc"  # 微軟正黑體 Bold


def shot(html_name, png_name, label, width=1120, height=800):
    """以 Playwright 截取本地 HTML（2 倍解析度，供印刷使用）。"""
    from playwright.sync_api import sync_playwright

    dest = OUT / png_name
    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page(viewport={"width": width, "height": height},
                          device_scale_factor=2)
        page.goto((ROOT / html_name).as_uri(), wait_until="load")
        page.wait_for_timeout(400)
        page.locator("body").screenshot(path=str(dest))
        b.close()
    print(f"{label}:", dest, Image.open(dest).size)


def fig4():
    """三張實拍等高併排，各加步驟標籤。"""
    srcs = [
        (IMG / "clinic_input_tool_20260817.jpg", "① 輸入評估"),
        (IMG / "clinic_discuss_1_20260817.jpg", "② 調出成效"),
        (IMG / "clinic_discuss_2_20260817.jpg", "③ 共同決定下一步"),
    ]
    # 版面只有 14.66cm 寬，圖太高會讓標籤列相對變細、印出來看不見，
    # 因此壓低單張高度、加大標籤列與字級（實測約等於內文 10pt）
    H = 520          # 每張統一高度
    GAP = 16
    BAR = 88         # 標籤列高度
    PAD = 10

    tiles = []
    for path, label in srcs:
        im = Image.open(path).convert("RGB")
        w = round(im.width * H / im.height)
        tiles.append((im.resize((w, H), Image.LANCZOS), label))

    total_w = sum(t.width for t, _ in tiles) + GAP * (len(tiles) - 1) + PAD * 2
    canvas = Image.new("RGB", (total_w, H + BAR + PAD * 2), "white")
    d = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(FONT, 52)

    x = PAD
    for im, label in tiles:
        canvas.paste(im, (x, PAD))
        d.rectangle([x, PAD + H, x + im.width, PAD + H + BAR], fill="#1B4332")
        tw = d.textlength(label, font=font)
        d.text((x + (im.width - tw) / 2, PAD + H + 18), label, font=font, fill="white")
        x += im.width + GAP

    dest = OUT / "fig4_clinic_steps.png"
    canvas.save(dest, quality=95)
    print("圖四:", dest, canvas.size)


if __name__ == "__main__":
    shot("fig1_flow.html", "fig1_flow.png", "圖一", height=760)
    # 圖二原為輸入工具實際操作截圖，2026-08-18 使用者要求改為概念圖
    # （實際畫面把欄位配置與病歷貼稿樣板整套曝光，怕被照抄）
    shot("fig2_datalayer.html", "fig2_datalayer.png", "圖二", height=820)
    fig4()
