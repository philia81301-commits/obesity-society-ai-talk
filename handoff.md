# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。
> 本檔只放交接必需的精簡資訊，完整脈絡與決策原因放 Obsidian `obesity-society-ai-talk/專案工作流程.md`。

## ⏯️ 目前做到哪

**2026-10-27（醫院機 X108521）12/13 場第Ⅲ段資安更新，全冊 59 頁，PPTX v10 已匯**：

- 使用者指示「舊的資料刪除以最新的取代」：刪 Strava（2018）／Netflix（2006）／郵遞區號（2000）三案，**沿用 data-slide 43–45** 改為：
  - P43「AI 讓攻擊變快：2026 資安現況」——27 秒（CrowdStrike）／141 個（Google GTIG，2026 1–8 月 vs 2025 全年 127）／247 天（IBM）＋醫療業外洩成本 664 萬美元連續 13 年最高
  - P44「案例：PHP2Shell 漏洞（2026 年 10 月）」——日相高市早苗 10/21 呼籲修補；中間卡用白話說明 PHP 是什麼；收束句「講者工具全為 HTML＋JS 靜態網頁，不用 PHP、不自架伺服器」
  - **P44.1「風險入口在哪裡」（新頁）**——左圖 `images/p44_php2shell_markers.png`（gpt-image-2 底圖＋PIL 編號），右欄原生文字圖說（CSS `.risk-legend`）：①–③ PHP 伺服器入口、④⑤ 靜態網頁仍有的入口（託管帳號、使用者電腦）、✓ 無伺服器程式。含圖說完整版 `images/p44_php2shell_risk_entry.png` 可單獨分享
  - P45「AI 本身成為新破口」——影子 AI 20%→43%、AI 程式碼 45% 含漏洞、提示詞注入逾 90 組織、92% 缺 AI 存取控管；新圖示 `#ic-code`
- 連動：P41 預告句、P47 左欄「下游：事後防堵」＋右欄「靜態網頁，無伺服器程式可攻擊」、P48 出處列。
- 引文與查證寫在各頁 HTML 註解；講稿 P43／P44／P44.1／P45 入 `<aside class="notes">`＋`content/speaker-notes-1213.md`。
- **PPTX v10 可編輯版**：59 頁、734 文字方塊、25.7 MB，OneDrive `文件\演講\2026演講\台灣肥胖醫學會1213\台灣肥胖醫學會1213_AI在肥胖治療_潘湘如_v10_可編輯_20261027.pptx`；python-pptx 驗證 P47–50 備忘稿開頭為【講稿】。**v9 使用者已自行刪除**。

**前一輪 2026-10-20（醫院機）**：12/13 場插入 3D 體型掃描＋NeRF 4 頁（P13.1–13.4，引用全部 ≥2021）、P50.05 沉浸式作品、P50.1–50.2 訓練場域、
講稿機制（`aside.notes` → PPTX 備忘稿【講稿】）、封面／頁尾改 12/13 場名＋新封面底圖；PPTX v9（已被 v10 取代）。

**更早輪次**（細節見 git log 與 Obsidian `專案工作流程.md`）：2026-09-16 P12 出處補查＋v8（家用）；09-15 可編輯 PPTX v7 機制；
09-10 字級底線清查；09-08 資料更新＋字級放大；08-18 會訊專論交稿。

## 🚦 目前狀態

- **HTML 簡報 59 頁（12/13 場版）**：可運行、離線可播；新頁皆實測（1280×720 截圖、孤字 0、<16px 0；P44.1 圖底約佔高 0.90 壓線）。
- **PPTX v10 可編輯版（2026-10-27）＝12/13 場現行版**；9/20 場的 v8 在 OneDrive `肥胖醫學會南區研討會\`。
- `slides/spec.yaml` 未同步 12/13 版（使用者表示 12/13 時長不重要，不必配速）。
- 本機預覽：伺服器 port 8770 於 repo 根目錄，網址 `/slides/index.html`（office 機由 Obesity-lecture 的 launch.json `ai-talk-slides` 啟動）。

## ➡️ 下一步

1. 12/13 場名全稱／時長待使用者補（封面目前寫「2026 年台灣肥胖醫學會學術研討會｜2026 年 12 月 13 日」）。
2. 使用者若再逐頁指正：事實類先回原始文獻／報告核對；改完 `cd slides && python build_fonts.py` → 實測 → 重匯 PPTX（v11 起跳）：
   `cd slides && python build_pptx_editable.py "<OneDrive>\台灣肥胖醫學會1213\..._v11_可編輯_<日期>.pptx"`（8770 要開著）。
3. 在別台電腦確認 OneDrive `台灣肥胖醫學會1213\` 有 v10（office 機 OneDrive.exe 常沒在跑，本輪已手動啟動）。

## ⚠️ 注意事項

### 本輪新增（2026-10-27）

- **資安段數字的底線**：商業周刊 2031 期剪報只當線索。「漏洞武器化少於 24 小時」查無原文、「88% 企業試用 AI 代理」與 IBM 原文 88%（資安投資意願增幅）不符 → 未採用；
  Capcom 1,177 萬筆外洩與 PHP2Shell 關聯**未證實**，只放講稿不上畫面；日本 112 起外洩分析未見「AI 被濫用」的已證實案例，**別講成 AI 已造成攻擊**。
- **「工具無 PHP」的根據**：掃 10 個工具 repo（.php／.htaccess／composer.json／wp-config 皆 0），皆為 GitHub Pages 靜態網頁。新增工具若改用自架伺服器，P44／P44.1 說法要改。
- 疊中文字的 PIL 腳本在 session scratchpad（未入庫）；要改 P44.1 圖：底圖 `slides/generated/p44_php2shell_20261027_143149_1.png`（不進 git，只在 office 機），
  標記座標 ①(470,455) ②(330,205) ③(640,640) ④(1150,120) ⑤(1215,700) ✓(1278,560)，字型 msjhbd／arialbd。
- 工具坑：`python -I` 會忽略 `PYTHONIOENCODING`，印中文變亂碼（資料本身沒壞）；Python 字串寫 Windows 路徑 `\2026` 要用 raw string 或雙反斜線，
  單反斜線會被當八進位跳脫（本輪 handoff 一度出現「演講6演講」即此）。


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

- 時間：2026-10-27（醫院機 X108521／office 帳號，12/13 場第Ⅲ段資安更新＋P44.1＋PPTX v10）
- 更新者：Claude Code（Opus 5.5）@ X108521
- Git push：✅ 已推（`3dbff69`）
- L3 Obsidian：已補（`2ndBrain/obesity-society-ai-talk/專案工作流程.md`）
- 前一筆：2026-10-20 @ X108521 · ✅ 已推（`0049f55`）
