# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。
> 本檔只放交接必需的精簡資訊，完整脈絡與決策原因放 Obsidian `obesity-society-ai-talk/專案工作流程.md`。

## ⏯️ 目前做到哪

**2026-09-15（醫院電腦 X108521）可編輯 PPTX v7**：

- 使用者要求「匯出可編輯 PPTX，改動會呈現」。v6 是整頁截圖，文字改不動，所以新寫兩支腳本：
  - `slides/build_pptx_editable.py`：Playwright 先把每頁文字設透明再截圖，當**投影片背景**（`<p:bg>`，
    圖標／圖表／底色都在，但點不到、拖不動）；文字依 DOM 逐段量位置、字級、粗細、顏色、行高、字距，
    用 python-pptx 放成原生文字方塊疊回原位（51 頁共 630 個）。備忘稿仍寫入全文。
  - `slides/pptx_fonts.py`：把 `fonts/*-subset.woff2`（變體字型）用 fontTools 切成 Regular／Bold／Black
    靜態實例（快取 `fonts/embed/`，不進 git），交給 Windows `t2embed.TTEmbedFont` 產 EOT 嵌進 PPTX，
    任何電腦打開都是 Noto Serif／Sans TC，**不必安裝字型**。子集含 Big5 常用字約 5,400 字。
- **成品 v7**：51 頁、26 MB，
  `C:\Users\office\OneDrive\文件\演講\2026演講\肥胖醫學會南區研討會\肥胖醫學會南區研討會_AI在肥胖治療_潘湘如_v7_可編輯_20260915.pptx`
  ＋副本 `F:\南區\`（使用者當日拿 v6 的位置）。v6 截圖版保留作備援播放。
- 驗證方式：PowerPoint COM 逐頁轉圖與瀏覽器原版疊圖比對（中位灰階差 2.2／255，最大是封面立體字）；
  嵌入字型用「檔案總管開啟＋螢幕截圖」確認封面與 P10 皆為宋體。
- 已知限制：SVG 內文字（圖表軸標）與右下頁碼在底圖裡不可編輯；PowerPoint 折行點偶爾與 HTML 差一兩字；
  封面立體字改用單層陰影近似；改字後底圖上的框線不會跟著長。

**2026-09-10（醫院電腦 X108521）字級 16px 底線清查輪＋PPTX v6**：

- **字級鐵則全面清查**（依記憶 `slide-typography-rules`）：base 46px 與 `.cite` 13px 原本已到位，
  但清查出 **15 個註記類 class 共 126 處**小字（12.5–15.6px，皆 em 基準）：
  sec-mark／ct-kind／ct-name／ct-step／cb-foot／caveat／ss-key／shot figcaption／
  fs-cap／ph-era／qr-cap／live-empty／live-foot／cn-step／bar-fill，
  一律改**固定 16px**（不用 em，避免 P5 那種複合縮放事故）。
  頁尾 footer-brand（13px）與頁碼（14px）屬裝飾例外，維持不動。
- **驗證**：<16px 非出處文字歸零；全 51 頁佔高 ≤0.90
  （P25 曾衝 0.903，`.shot figcaption` padding 7→5px 後收回 0.897；現最高 P10＝0.900 壓線過）；
  無新孤字（案例 03 側欄手動斷行維持正常）；無文字內容變更，**免重跑 build_fonts.py**。
- **PPTX v6 已重匯**：51 頁、30.3 MB，
  存 `C:\Users\office\OneDrive\文件\演講\2026演講\肥胖醫學會南區研討會\肥胖醫學會南區研討會_AI在肥胖治療_潘湘如_v6_20260910.pptx`
  （與 v1–v5 同資料夾、同命名系列；家用機對應 `C:\Users\phili\OneDrive\文件\演講\...`）。**v5 作廢，v6 為繳交版**。
  轉檔走 8770＋`SLIDES_URL`，事前 `curl` 驗證 51 個 `<section>` 無誤；成品抽驗 P10／P51 皆正確。
  ⚠️ 曾誤存 `D:\潘湘如\演講\`（收工時發現 L3 筆記早已記載該處**不是** OneDrive，已搬正並刪誤放副本）。
- **另一 session 產出**：`content/exam-questions-ch11-20260910.md`（肥胖專科醫師命題 8 題備選，
  v4 定案選 1／3／4／5／7／8 共 6 題；定稿 DOCX `肥胖專科醫師命題_定稿6題_20260910.docx` 存 OneDrive 不進 git）。

**先前輪次摘要**（細節見 git log 與 Obsidian）：

- **2026-09-09（醫院機）P51 底圖輪**：gpt-image-2 封底底圖 duotone 重上色掛載（opacity 0.12）；port 改 8770。
- **2026-09-09（家用機）語句與版面校對輪**：S1–S51 逐頁去誇大／去口語、內部查證筆記移出畫面、
  13px 內容字升級 quote-box／key-box、孤字歸零、P51 整頁重設計。
- **2026-09-08（醫院機）三輪**：資料更新至 2026-08 月報（v3）→ base 42→46px（v4）→ P6 事實修正（v5）。
- **2026-08-18（家用）階段八會訊專論**：當日交稿完成（12 頁、4,198 字），定稿在 OneDrive。

## 🚦 目前狀態

- **HTML 簡報（51 頁）**：可運行、離線可播、字級全面達鐵則底線、孤字歸零、佔高全數 ≤0.90。
- **PPTX v7 可編輯版（2026-09-15）＝現行繳交／修改版**；v6 截圖版保留作備援播放；v1–v5 供追溯。
- 專論已定稿可投（OneDrive）；repo 內仍殘留 Word 鎖定檔與作廢舊標題 DOCX（不進 git，可刪）。
- 命題定稿 6 題已產出 DOCX（OneDrive），備選題庫 md 在 repo `content/`。

## ➡️ 下一步

1. 演講日 **2026-09-20**：剩排練（51 頁配 40 分鐘）。
2. 使用者若再逐頁指正：事實類先調文獻原文核對；語句類套用「專業醫師口吻」原則
   （見記憶 `slide-content-style-rules`）；改完重測佔高＋孤字、**重匯可編輯 PPTX（v8 起跳）**：
   `cd slides && python build_pptx_editable.py "<OneDrive 路徑>\..._v8_可編輯_<日期>.pptx"`
   （需先開 8770 伺服器；可加第二個參數只匯指定頁測試，如 `1,10`）。
3. （選辦）OneDrive 資料夾裡 v1–v5 若要清理，由使用者決定（勿自動刪）。

## ⚠️ 注意事項

### 本輪新增（2026-09-15）

- **🩸 PowerPoint COM 的 `Slide.Export` 轉圖不會套用嵌入字型**——用它驗證嵌入字型會誤判「沒生效」
  （2026-09-15 白繞了一小時）。要驗證嵌入字型，用 `Start-Process` 一般開啟＋螢幕截圖。
  COM 轉圖仍可用來比對版面位置。
- 手刻 EOT 表頭 PowerPoint 不收（t2embed 回 E_FONTDATAINVALID：少 XOR 旗標、名稱字串缺 NUL）；
  一律用 `t2embed.TTEmbedFont` 產。字型以 `AddFontResourceEx(FR_PRIVATE)` 私有載入，不動系統。
- `build_pptx_editable.py` 的兩個踩坑：大字兩行的字面矩形會互相重疊，分行要用行高門檻不能用重疊判斷；
  `color-mix()` 算出來的顏色是 `color(srgb …)` 格式，解析器要另外處理。
- 醫院機 PowerPoint 是 **2016**（非 M365）。

### 2026-09-10

- **字級規範自本輪起的完整版**：承載文字的註記類 class 一律**固定 16px** 以上（不用 em）；
  純出處列 `.cite` 13px、頁尾 footer-brand／頁碼 13–14px 屬例外；
  承載觀眾內容的說明用 quote-box（24.8px）以上；標籤 chip 至少 19px。
  改字級後必測：<16px 掃描歸零＋全頁佔高 ≤0.90＋孤字檢測（詳見記憶 `slide-typography-rules`）。
- P10 佔高 0.900 剛好壓線——該頁再加任何內容前先想瘦身。
- **🩸 醫院機 `D:\潘湘如\演講\` 不是 OneDrive**（agents.md 舊註「應為同一掛載點」已證偽並修正）：
  成品一律存 `C:\Users\office\OneDrive\文件\演講\2026演講\...`，命名沿用
  `肥胖醫學會南區研討會_AI在肥胖治療_潘湘如_v<N>_<日期>.pptx`。

### 既有（未變動）

- **🩸 port 8765 兩台電腦都會撞**——`Obesity-lecture`（9/13 場）server 佔用中。
  醫院機 `.claude/launch.json` 已改 **8770**；家用機曾臨時用 8899。
  轉 PPTX 前先關掉別場伺服器或指定 `SLIDES_URL`，並 `curl` 驗證 51 個 `<section>`。
- 醫院機有一筆已被遠端取代的 stash（舊 P51 修改），無影響，可 `git stash drop`。
- draw 技能輸出目錄為 `slides/generated/`（非 `slides/images/generated/`），已補進 .gitignore。
- **內部查證筆記不上畫面**（使用者鐵律，已存記憶 `slide-content-style-rules`）：
  「已依 reference/xxx 查證」「疑似幻覺已刪除」類文字一律放 HTML 註解或 reference/。
- **P9 事實底線**：成人肥胖指引 2025〈科技與虛擬醫療〉由講者本人執筆（AI 聊天機器人／CDSS 各 2C）。
  任何「AI 未被指引收錄」的表述都要先核對這份指引。
- 改 `slides/index.html` 內文後原則上重跑 `build_fonts.py`（可先用 fontTools 比對省略）；emoji 不在字型內。
- 離線原則：`slides/index.html` 不得出現 CDN 連結。
- `build_pptx.py` 不可用 `wait_until="networkidle"`（Firebase 長連線必逾時）；
  X108521 沒裝 chromium，一律 `channel="chrome"`（已內建 fallback）。
- GitHub Pages 靜態資源 10 分鐘快取；新圖不可命名 `cover_*.png`（.gitignore 擋）。
- repo 公開：門診數據去識別化、聚合呈現；換診間照片前必讀 `reference/clinic-photo-redaction-20260817.md`。
- 引用外部指引改寫為摘述（講者自己的著作不在此限）。
- 醫院電腦 X108521：外連下載被擋（build_fonts.py 會失敗）、`convert` 非 ImageMagick、
  Playwright 用 chrome channel；office 帳號 Obsidian vault：`C:\Users\office\OneDrive\2ndBrain`。
- 專論退修流程：改 `content/article-newsletter-2026.md` → `cd article && python build_docx.py "<檔名>.docx"`；
  勿動 `build_docx.py` 的 `ANCHORS` 句（錨點失配時是去更新 ANCHORS，不是改回內文）。
  文獻一律 NCBI E-utilities 查證（PubMed 網頁版擋 cookie，esummary API 可直取）。
  Word COM 用 `win32com.client.Dispatch`（PowerShell PIA 會拋 TYPE_E_CANTLOADLIBRARY）；
  接上使用者開啟的 Word 實例時**絕不呼叫 `app.Quit()`**。
  Gmail／Drive MCP 傳不了大附件（base64 超上限），寄檔請使用者自己拖曳。

## 🕐 最後更新

- 時間：2026-09-15（醫院機，可編輯 PPTX 輪，尚未正式收工）
- 更新者：Claude Code（Fable 5.1）@ X108521（醫院）
- 階段：**可編輯 PPTX v7 已匯**（OneDrive＋F:\南區），腳本已入庫，剩排練
- Git push：✅ 已推（`cf1b33d`）
- L3 Obsidian：⏳ 本輪未更新（收工時補）
- 前一筆：2026-09-10 @ X108521（醫院）· ✅ 已推（`6e1c273`）
