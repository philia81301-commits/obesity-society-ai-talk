"""產生 P2 觀眾作答用的 QR code。

網址不寫死在這裡，而是從 live-config.js 的 audienceUrl 讀出來，
避免「改了網址卻忘了重畫 QR」這種現場才會爆的錯。

    cd slides && python build_qr.py

輸出：slides/images/qr_audience.png
"""

import re
import sys
from pathlib import Path

try:
    import qrcode
    from qrcode.constants import ERROR_CORRECT_H
except ImportError:
    sys.exit("缺少 qrcode 套件，請先執行：pip install qrcode[pil]")

HERE = Path(__file__).resolve().parent
CONFIG = HERE / "live-config.js"
OUT = HERE / "images" / "qr_audience.png"


def read_audience_url() -> str:
    text = CONFIG.read_text(encoding="utf-8")
    m = re.search(r"audienceUrl\s*:\s*['\"]([^'\"]+)['\"]", text)
    if not m:
        sys.exit(f"在 {CONFIG.name} 找不到 audienceUrl 設定")
    return m.group(1)


def main() -> None:
    url = read_audience_url()

    # ERROR_CORRECT_H：容錯率 30%，投影幕反光或觀眾手抖時仍掃得到。
    # box_size 22 讓輸出約 700–900 px，投影後仍夠銳利。
    qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=22, border=2)
    qr.add_data(url)
    qr.make(fit=True)

    # 深墨綠（#1B4332）配白底，與簡報主色一致；掃描對比度仍足夠。
    img = qr.make_image(fill_color="#1B4332", back_color="white")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)

    print(f"網址：{url}")
    print(f"已輸出：{OUT.relative_to(HERE)}　({img.size[0]}×{img.size[1]} px)")


if __name__ == "__main__":
    main()
