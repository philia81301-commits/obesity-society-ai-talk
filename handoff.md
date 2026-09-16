# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。
> 本檔只放交接必需的精簡資訊，完整脈絡與決策原因放 Obsidian `obesity-society-ai-talk/專案工作流程.md`。

## ⏯️ 目前做到哪

**2026-09-16（家用機 DESKTOP-LVSV9Q5）P12 出處補查＋改字＋可編輯 PPTX v8**：

- **P12 出處補查**：使用者在 P12 截圖標了 [1] GRS 卡、[2] TiP DecScore 卡、[3] 結論句，派三個 subagent
  平行查（PubMed／Europe PMC／Crossref／OpenAlex／ClinicalTrials.gov／官方政策文件），整合為
  `reference/p12-glp1-ai-source-check-20260916.md`：§0 改字總表、§1–2 兩篇的正式引用與逐項核對、
  §3 結論句的佐證＋**同行反駁 8 條**＋建議講稿、各節「查不到」清單、OR/p 值解讀（備忘稿用）。
  關鍵發現：GRS 摘要有正式增刊引用（*Gastroenterology* 2025;169(1 Suppl):S-946，DDW Su2057）但**仍無全文**；
  TiP DecScore 是回溯資料、醫師開藥時未見分數，且**全體世代亦顯著**（55.1% vs 47.4%，P=0.028），
  8/14 筆記的「57.9% vs 28.6%」是誤讀（模型建議比例，非療效）；Acosta 2021 表型導向 15.9% vs 9.0%
  **非隨機**（更正啟事），Mayo 真正的 RCT NCT03374956 幾乎無差且未發表。
- **P12 改字**（`slides/index.html`＋`slides/spec.yaml`，使用者「照建議更正」）：
  左卡「基因風險分數（CTS-GRS）預測噁心風險」、註腳 `Mayo／Phenomix｜Gastroenterology 2025 增刊（DDW Su2057）｜
  liraglutide 組 post-hoc，有基因資料 n=110｜OR 5.0，p=0.0058`；右卡「TiP DecScore：處方與模型建議一致與否」、
  標籤「處方恰與建議一致／12 個月 HbA1c <7% 達標率」vs「不一致者」、註腳 `Shi et al., Commun Med 2026;6:165｜
  上海回溯世代（醫師開藥時未見分數），12 個月 n=829｜全體 55.1% vs 47.4%，P=0.028`、caveat「<55 歲亞組，P=0.001」。
  結論句不動。瀏覽器實測：兩卡標題各一行、註腳各兩行、佔高 545/720（<648）、`build_fonts.py` 重跑無缺字。
- `reference/citation-verification.md` 主張 4／7 各補一則 2026-09-16 引用區塊註記（原文未刪）。
- **同日稍早另一 session（未收工）的 P8 修正一併入庫**：Warwick 數字卡 450 人／4 家醫院→
  JMIR 2025;27:e62661 單院 n=412、App 組每月多減 0.74 kg（詳見 index.html P8 的 HTML 註解）。
- **PPTX v8 可編輯版已匯**：51 頁、630 文字方塊、26.6 MB、四家族字型嵌入，**含 P8＋P12 兩處修正**，
  `C:\Users\phili\OneDrive\文件\演講\2026演講\肥胖醫學會南區研討會\肥胖醫學會南區研討會_AI在肥胖治療_潘湘如_v8_可編輯_20260916.pptx`
  （醫院機對應 `C:\Users\office\OneDrive\...`，OneDrive 同步後即可拿到）。驗證：python-pptx 讀 P12 20 個文字方塊皆新版、
  備忘稿同步、6 個 fntdata；PowerPoint COM 轉圖 P12 與瀏覽器原版灰階差中位 0/255。
- **修 `slides/pptx_fonts.py`**：第一次匯出在嵌字型時失敗——家用機系統裝了完整版 Noto Serif TC（16.8 MB VF），
  與腳本 FR_PRIVATE 載入的靜態子集**同名**，GDI 選字選到系統那份被防呆檢查擋下。改為優先
  `TTEmbedFontFromFileA` 直接指定字型檔（不經 GDI 選字），失敗才退回舊路徑；六個字型檔單測皆走新路徑成功。
- `slides/build_summary_docx.py`（2026-09-13 家用機產一頁摘要 DOCX 的腳本，先前未入庫）一併入庫。

**前一輪：2026-09-15（醫院電腦 X108521）可編輯 PPTX v7**：新寫 `build_pptx_editable.py`（文字設透明截圖當
`<p:bg>` 背景＋DOM 量測放 630 個原生文字方塊＋備忘稿）與 `pptx_fonts.py`（子集切 Regular／Bold／Black 靜態實例，
t2embed 產 EOT 嵌入）。v7 存 OneDrive＋`F:\南區\`。已知限制：SVG 內文字與頁碼在底圖不可編輯；PowerPoint 折行點偶爾差一兩字；
封面立體字單層陰影近似；改字後底圖框線不會跟著長。**v8 已取代 v7**。

**更早輪次摘要**（細節見 git log 與 Obsidian）：2026-09-10 字級 16px 底線清查＋PPTX v6（醫院）；
2026-09-09 P51 底圖（醫院）／語句與版面校對（家用）；2026-09-08 資料更新→字級放大→P6 修正 v3–v5（醫院）；
2026-08-18 會訊專論交稿（家用）。

## 🚦 目前狀態

- **HTML 簡報（51 頁）**：可運行、離線可播、字級達鐵則底線、孤字歸零、佔高全數 ≤0.90；P8／P12 為 2026-09-16 版。
- **PPTX v8 可編輯版（2026-09-16）＝現行繳交／修改版**；v6 截圖版保留作備援播放；v7 已被 v8 取代（可留可刪，使用者決定）。
- 一頁摘要 DOCX／PDF（2026-09-13）已在 OneDrive；專論已定稿可投；命題定稿 6 題 DOCX 在 OneDrive。
- 本機預覽：`.claude/launch.json` 的 `talk-preview`（`python -m http.server 8770` 於 repo 根目錄），匯 PPTX 時直接沿用同一個伺服器。

## ➡️ 下一步

1. 演講日 **2026-09-20**：剩排練（51 頁配 40 分鐘）。P12 講法先讀 `reference/p12-glp1-ai-source-check-20260916.md`
   §1.3「OR 5.0／p=0.0058 怎麼解讀」、§3.5 同行反駁、§3.7 建議講稿。
2. 使用者若再逐頁指正：事實類先調文獻原文核對；語句類套「專業醫師口吻」（記憶 `slide-content-style-rules`）；
   改完 `cd slides && python build_fonts.py` → 測佔高＋孤字 → **重匯可編輯 PPTX（v9 起跳）**：
   `cd slides && python build_pptx_editable.py "<OneDrive 路徑>\..._v9_可編輯_<日期>.pptx"`
   （8770 伺服器要開著；第二個參數可只匯指定頁測試，如 `1,12`）。
3. （選辦，使用者未決定）`content/article-newsletter-2026.md` 參考文獻 [1] 標題少 "Receptor"、可升級為正式增刊引用；
   內容本身無誤，不改也可。
4. （選辦）OneDrive 內 v1–v5、v7 若要清理，由使用者決定（勿自動刪）。

## ⚠️ 注意事項

### 本輪新增（2026-09-16）

- **🩸 家用機系統裝了 Noto Serif TC（完整 VF）**，與嵌入用靜態子集同名。`pptx_fonts.py` 已改走 `TTEmbedFontFromFileA`；
  若再看到「GDI 選到別的字型（16855236 vs …）」就是這個問題，不要去動系統字型。
- **P12 講法底線**：OR 5.0 **不要講成「風險 5 倍」**（比例 68/30≈2.3 倍，新聞稿原句 "more than twice as likely"）；
  「處方恰與模型建議一致」≠「依 AI 建議用藥」（醫師沒看過分數）；GRS 卡 n=110 含安慰劑組、噁心比較限 liraglutide 組
  （每格事件數推估 9–17 人，屬小樣本）；同一 CTS-GRS 在療效上方向相反（低分減重較好），別說「高 GRS＝反應好」。
- **8/14 `citation-verification.md` 的「57.9% vs 28.6%」是誤讀**（模型建議 GLP-1RA／SGLT-2i 的病人比例），已補註，備忘稿別再用。
- 工具坑：Bash heredoc 超過約 20 KB 會解析失敗（單引號被當 shell 引號）→ 大檔改用 Write 工具；
  Python 印中文要 `PYTHONIOENCODING=utf-8`，否則 Git Bash console 亂碼（腳本其實有跑成功）；
  Bash 的 `$TMP` 是 `C:\Users\phili\AppData\Local\Temp`，不是 scratchpad。
- PowerPoint COM `Slide.Export` 可用來比對版面（本輪 P12 灰階差中位 0），但**不會套嵌入字型**（見 09-15 條）。

### 2026-09-15

- **🩸 PowerPoint COM 的 `Slide.Export` 轉圖不會套用嵌入字型**——用它驗證嵌入字型會誤判「沒生效」。
  要驗證嵌入字型，用 `Start-Process` 一般開啟＋螢幕截圖。COM 轉圖仍可用來比對版面位置。
- 手刻 EOT 表頭 PowerPoint 不收（t2embed 回 E_FONTDATAINVALID：少 XOR 旗標、名稱字串缺 NUL）；一律用 t2embed 產。
- `build_pptx_editable.py` 的兩個踩坑：大字兩行的字面矩形會互相重疊，分行要用行高門檻不能用重疊判斷；
  `color-mix()` 算出來的顏色是 `color(srgb …)` 格式，解析器要另外處理。
- 醫院機 PowerPoint 是 **2016**（非 M365）；家用機為 M365（`C:\Program Files\Microsoft Office\root\Office16`）。

### 2026-09-10

- **字級規範完整版**：承載文字的註記類 class 一律**固定 16px** 以上（不用 em）；純出處列 `.cite` 13px、
  頁尾 footer-brand／頁碼 13–14px 屬例外；承載觀眾內容的說明用 quote-box（24.8px）以上；標籤 chip 至少 19px。
  改字級後必測：<16px 掃描歸零＋全頁佔高 ≤0.90＋孤字檢測（詳見記憶 `slide-typography-rules`）。
- P10 佔高 0.900 剛好壓線——該頁再加任何內容前先想瘦身。
- **🩸 醫院機 `D:\潘湘如\演講\` 不是 OneDrive**：成品一律存 `C:\Users\office\OneDrive\文件\演講\2026演講\...`，
  命名沿用 `肥胖醫學會南區研討會_AI在肥胖治療_潘湘如_v<N>_<日期>.pptx`。

### 既有（未變動）

- **🩸 port 8765 兩台電腦都會撞**——`Obesity-lecture`（9/13 場）server 佔用中。兩台 `.claude/launch.json` 皆已用 **8770**。
  轉 PPTX 前確認 8770 指到本專案（`curl` 驗證 51 個 `<section>`），或指定 `SLIDES_URL`。
- 醫院機有一筆已被遠端取代的 stash（舊 P51 修改），無影響，可 `git stash drop`。
- draw 技能輸出目錄為 `slides/generated/`（非 `slides/images/generated/`），已在 .gitignore。
- **內部查證筆記不上畫面**（使用者鐵律，記憶 `slide-content-style-rules`）：查證出處放 HTML 註解或 `reference/`。
- **P9 事實底線**：成人肥胖指引 2025〈科技與虛擬醫療〉由講者本人執筆（AI 聊天機器人／CDSS 各 2C）。
  任何「AI 未被指引收錄」的表述都要先核對這份指引。
- 改 `slides/index.html` 內文後重跑 `build_fonts.py`（兩台的 `*-VF.ttf` 來源檔都在，不會觸發下載）；emoji 不在字型內。
- 離線原則：`slides/index.html` 不得出現 CDN 連結。
- `build_pptx.py` 不可用 `wait_until="networkidle"`（Firebase 長連線必逾時）；X108521 沒裝 chromium，一律 `channel="chrome"`。
- GitHub Pages 靜態資源 10 分鐘快取；新圖不可命名 `cover_*.png`（.gitignore 擋）。
- repo 公開：門診數據去識別化、聚合呈現；換診間照片前必讀 `reference/clinic-photo-redaction-20260817.md`。
- 引用外部指引改寫為摘述（講者自己的著作不在此限）。
- 醫院電腦 X108521：外連下載被擋、`convert` 非 ImageMagick、Playwright 用 chrome channel；
  office 帳號 Obsidian vault：`C:\Users\office\OneDrive\2ndBrain`。
- 專論退修流程：改 `content/article-newsletter-2026.md` → `cd article && python build_docx.py "<檔名>.docx"`；
  勿動 `build_docx.py` 的 `ANCHORS` 句。文獻一律 NCBI E-utilities 查證。Word COM 用 `win32com.client.Dispatch`；
  接上使用者開啟的 Word 實例時**絕不呼叫 `app.Quit()`**。Gmail／Drive MCP 傳不了大附件。

## 🕐 最後更新

- 時間：2026-09-16（家用機，P12 補查＋改字＋PPTX v8 輪）
- 更新者：Claude Code（Opus 5）@ DESKTOP-LVSV9Q5（家用）
- 階段：**PPTX v8 已匯**（OneDrive），P8／P12 修正已入 HTML 與 PPTX，剩排練
- Git push：✅ 已推（`283bef1`）
- L3 Obsidian：✅ 已補（含 09-15 欠的 v7 紀錄）
- 前一筆：2026-09-15 @ X108521（醫院）· ✅ 已推（`cf1b33d`／`d255940`）
