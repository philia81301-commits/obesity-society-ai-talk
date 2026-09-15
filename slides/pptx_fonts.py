"""把 Noto Sans TC / Noto Serif TC 子集字型嵌進 PPTX（build_pptx_editable.py 用）。

為什麼要嵌：可編輯 PPTX 的文字方塊靠 PowerPoint 即時排版，機器上沒裝 Noto Serif TC 時
標題會被換成新細明體，整份風格走樣。嵌進檔案後，任何機器打開都用原字型，不必安裝。

做法：
  1. fonts/*-subset.woff2 是變體字型（wght 軸），PowerPoint 只認 Regular／Bold 兩檔，
     所以用 fontTools instancer 切出 400（Regular）、700（Bold）兩個靜態實例，
     900 另立一個家族「<家族> Black」（封面標題、大數字用）。
  2. 靜態 TTF 交給 Windows t2embed（TTEmbedFont）包成 EOT（MTX 壓縮）→ ppt/fonts/fontN.fntdata，
     presentation.xml 加 <p:embeddedFontLst>。Noto 系列 OFL 授權、fsType=0，可自由嵌入。
  3. 子集只含 Big5 常用字約 5,400 字＋本簡報用到的符號；改標題時打到罕用字會退回替代字型。

切好的靜態檔快取在 fonts/embed/（不進 git）。
"""

import ctypes
import io
import struct
from ctypes import wintypes
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from lxml import etree
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx.opc.package import Part
from pptx.opc.packuri import PackURI
from pptx.oxml.ns import qn

HERE = Path(__file__).parent
FONTS = HERE / "fonts"
CACHE = FONTS / "embed"

# (家族名, 來源子集, 樣式→wght)
FAMILIES = [
    ("Noto Sans TC", "NotoSansTC-subset.woff2", {"regular": 400, "bold": 700}),
    ("Noto Sans TC Black", "NotoSansTC-subset.woff2", {"regular": 900}),
    ("Noto Serif TC", "NotoSerifTC-subset.woff2", {"regular": 400, "bold": 700}),
    ("Noto Serif TC Black", "NotoSerifTC-subset.woff2", {"regular": 900}),
]


def _rename(font: TTFont, family: str, style: str, weight: int) -> None:
    sub = {"regular": "Regular", "bold": "Bold"}[style]
    full = family if style == "regular" else f"{family} {sub}"
    ps = (family.replace(" ", "") + "-" + sub)
    name = font["name"]
    name.names = [n for n in name.names if n.nameID not in (1, 2, 3, 4, 6, 16, 17)]
    for nid, val in ((1, family), (2, sub), (3, f"{ps};embed"), (4, full), (6, ps)):
        name.setName(val, nid, 3, 1, 0x409)
        name.setName(val, nid, 1, 0, 0)
    os2 = font["OS/2"]
    os2.usWeightClass = weight
    bold = style == "bold"
    os2.fsSelection = (os2.fsSelection & ~0b1100001) | (0b100000 if bold else 0b1000000)
    font["head"].macStyle = (font["head"].macStyle & ~1) | (1 if bold else 0)


def static_instance(src: Path, family: str, style: str, weight: int) -> Path:
    out = CACHE / f"{family.replace(' ', '')}-{style}.ttf"
    if out.exists() and out.stat().st_mtime >= src.stat().st_mtime:
        return out
    CACHE.mkdir(exist_ok=True)
    font = TTFont(src)
    font.flavor = None                       # woff2 → 純 TTF
    inst = instancer.instantiateVariableFont(font, {"wght": weight}, inplace=True, updateFontNames=False)
    _rename(inst, family, style, weight)
    inst.save(out)
    return out


_gdi = _user = _t2 = None


def _win():
    """延遲載入 Win32 API（只在真的要嵌字型時才碰）。"""
    global _gdi, _user, _t2, _WRITEPROC
    if _gdi is None:
        _gdi = ctypes.WinDLL("gdi32"); _user = ctypes.WinDLL("user32"); _t2 = ctypes.WinDLL("t2embed.dll")
        _gdi.CreateFontW.restype = ctypes.c_void_p
        _gdi.SelectObject.restype = ctypes.c_void_p
        _gdi.SelectObject.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        _gdi.DeleteObject.argtypes = [ctypes.c_void_p]
        _user.GetDC.restype = ctypes.c_void_p
        _user.ReleaseDC.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        _WRITEPROC = ctypes.WINFUNCTYPE(wintypes.ULONG, ctypes.c_void_p, ctypes.c_void_p, wintypes.ULONG)
        _t2.TTEmbedFont.argtypes = [ctypes.c_void_p, wintypes.ULONG, wintypes.ULONG, ctypes.c_void_p, ctypes.c_void_p,
                                    _WRITEPROC, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ushort, ctypes.c_ushort,
                                    ctypes.c_void_p]


def ttf_to_eot(ttf_path: Path, family: str, weight: int) -> bytes:
    """用 Windows t2embed 的 TTEmbedFont 產生 EOT（MTX 壓縮）。

    自己手刻 EOT 表頭被 PowerPoint 拒收（2026-09-15：缺 XOR 旗標、名稱字串少 NUL 結尾，
    t2embed 回 E_FONTDATAINVALID），所以改讓 Windows 自己產。
    字型以 FR_PRIVATE 載入，只在本程序可見，不動系統字型與登錄檔。
    """
    _win()
    data = ttf_path.read_bytes()
    path = str(ttf_path.resolve())
    if not _gdi.AddFontResourceExW(path, 0x10, None):          # FR_PRIVATE
        raise RuntimeError(f"AddFontResourceEx 失敗：{path}")
    hdc = _user.GetDC(None)
    hf = _gdi.CreateFontW(-40, 0, 0, 0, weight, 0, 0, 0, 1, 0, 0, 0, 0, family)
    old = _gdi.SelectObject(hdc, hf)
    try:
        def run(flags: int) -> bytes:
            out = io.BytesIO()

            @_WRITEPROC
            def wr(_stream, src, n):
                out.write(ctypes.string_at(src, n))
                return n

            priv = wintypes.ULONG(); st = wintypes.ULONG()
            rc = _t2.TTEmbedFont(hdc, flags, 1, ctypes.byref(priv), ctypes.byref(st), wr, None, None, 0, 0, None)
            if rc:
                raise RuntimeError(f"TTEmbedFont({family}) 失敗 rc={rc:#x}")
            return out.getvalue()

        # 先用未壓縮版驗證 GDI 選到的確實是這個檔（系統若裝了同名字型，GDI 可能挑到那一個）
        raw = run(0x0)
        font_size = struct.unpack_from("<I", raw, 4)[0]
        if font_size != len(data):
            raise RuntimeError(f"{family}：GDI 選到別的字型（{font_size} vs {len(data)} bytes），請檢查系統是否裝了同名字型")
        return run(0x4)                                        # TTEMBED_TTCOMPRESSED
    finally:
        _gdi.SelectObject(hdc, old); _gdi.DeleteObject(hf); _user.ReleaseDC(None, hdc)
        _gdi.RemoveFontResourceExW(path, 0x10, None)


def embed_fonts(prs) -> list[str]:
    """把 FAMILIES 全部嵌進 prs；回傳嵌入的家族名。"""
    pres_part = prs.part
    root = prs._element
    for old in root.findall(qn("p:embeddedFontLst")):
        root.remove(old)
    lst = etree.Element(qn("p:embeddedFontLst"))
    notes_sz = root.find(qn("p:notesSz"))
    notes_sz.addnext(lst)
    root.set("embedTrueTypeFonts", "1")
    root.set("saveSubsetFonts", "0")
    n = 0
    done = []
    for family, src_name, styles in FAMILIES:
        src = FONTS / src_name
        ef = etree.SubElement(lst, qn("p:embeddedFont"))
        first = None
        for style, weight in styles.items():
            ttf = static_instance(src, family, style, weight)
            n += 1
            part = Part(PackURI(f"/ppt/fonts/font{n}.fntdata"), "application/x-fontdata",
                        pres_part.package, ttf_to_eot(ttf, family, weight))
            rId = pres_part.relate_to(part, RT.FONT)
            if first is None:
                first = ttf
            etree.SubElement(ef, qn(f"p:{style}"), {qn("r:id"): rId})
        f = TTFont(first)
        pan = "".join(f"{b:02X}" for b in _panose_bytes(f))
        font_el = etree.Element(qn("p:font"), typeface=family, panose=pan, pitchFamily="34", charset="-120")
        ef.insert(0, font_el)
        done.append(family)
    return done


def _panose_bytes(font: TTFont) -> bytes:
    p = font["OS/2"].panose
    return bytes(getattr(p, f) for f in
                 ("bFamilyType", "bSerifStyle", "bWeight", "bProportion", "bContrast",
                  "bStrokeVariation", "bArmStyle", "bLetterForm", "bMidline", "bXHeight"))
