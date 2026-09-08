# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。
> 本檔只放交接必需的精簡資訊，完整脈絡與決策原因放 Obsidian `obesity-society-ai-talk/專案工作流程.md`。

## ⏯️ 目前做到哪

**2026-09-09（醫院電腦 X108521）P51 底圖輪（收工）**：

- **P51 封底底圖定案掛載**：gpt-image-2（low, 1536×1024）生成 2 張候選（NT$0.6），
  採用「羅盤＋地平線＋神經網路節點＋體重計＋下降曲線」版；因原圖綠色偏灰橄欖，
  以 PIL duotone 重上色為 `--accent #1B4332` × `--bg-alt #F6F5F0`，
  存 `slides/images/p51_qa_bg_duotone_20260909.png`，掛上 P51（cover、opacity 0.12），瀏覽器實測通過。
  候選原檔在 `slides/generated/`（已加入 .gitignore，不進 git）。
- **pull 回家用機校對輪**（`9ef14c8`＋`300a555`）：使用者在醫院看到「可介入」仍小字，
  原因是這台沒 pull——拉回後 P5 實測 19px 標籤正常。本機曾與遠端 P51 重設計重疊修改，
  以遠端版為準，僅重新掛上底圖；被取代的本機修改在 stash（可 `git stash drop` 清掉）。
- **port 衝突**：醫院機 8765 也被 `Obesity-lecture`（9/13 場）server 佔用，
  `.claude/launch.json` 改為 **port 8770**。

**2026-09-09（家用電腦 DESKTOP-LVSV9Q5）語句與版面校對輪**：使用者逐頁校對 S1–S51，
全部指正已處理完畢並實測驗證。**只改了 `slides/index.html`；PPTX v6 尚未重匯**。

- **語句去誇大、去口語（專業醫師口吻，形容詞減量）**：
  「漂亮數字」→成效、「最嚴謹」→證據等級最高、「掉到」→降至、「最煩／最酷」→最耗時的例行工作／最新的技術、
  「東西」→工具／依據、「被臨床現實逼出來」→從臨床的實際問題出發、「量體」→規模；
  P9 key-box 整段改寫（去掉「缺的不是想像力」）、P10 右框重寫（「引用時應同時說明的限制」）。
- **內部查證筆記全數移出畫面**（使用者原話「這種搜尋結果不要呈現，你應該要有這種基本判斷」）：
  P12／P13／P14／P15（整塊出處含評註刪除）／P37（方法學限制整塊刪除）。內容都留在原位的 HTML 註解裡備查。
- **承載內容的 13px 小字升級為正常字級**：P18（AI 兩層意義→quote-box）、P19（定位說明）、
  P21（既有文件）、P30（呼應Ⅲ段）、P42（對照講者工具）→quote-box；P46（三者共通風險）→key-box。
  純出處列（P27 病人同意聲明、P31／P35／P40／P48）維持 13px 不動。
- **字級 bug**：P5「可介入」標籤原本 `.3em`×`.5em` 複合縮成 **6.9px**，改固定 19px（15px 仍被使用者嫌小）。
- **行末孤字逐頁檢測**（Range.getClientRects 逐字分行）：排除 P14／P24×3／P25／P26／P28×2／P41／P50
  共 8 處；案例 03 側欄改「月度分析<br>自動化」手動斷行；P24「三格式產出」改名「報告產出」。
- **P51 整頁重設計**：工具連結四格移除，改為 Q&A＋「AI 提供地圖，醫師擔任嚮導」＋署名＋場次資訊。
- 驗證：全 51 頁佔高實測 **≤0.899**（P9 改寫曾衝到 0.918 已收回 0.817）、孤字歸零、
  fontTools 比對**無缺字**（免重跑 build_fonts.py）。

**2026-09-08（醫院電腦 X108521）三輪**：資料更新至 2026-08 月報＋維持期表單 bullet（v3）→
全簡報字級放大 base 42→46px、出處列固定 13px、P23 待補區塊移除（v4）→
P6 依 PMID 34335479 修正 n=2,495／HMO-I 與 LMO 圖例對調／引註頁碼＋「帶」錯字（**v5**）。

**2026-08-18（家用）階段八會訊專論**：當日交稿完成（12 頁、4,198 字），已定稿可投，成品在 OneDrive。

## 🚦 目前狀態

- **HTML 簡報（51 頁）**：最新版＝校對輪＋P51 底圖，可運行、離線可播、孤字歸零。
  P51 底圖為新增 PNG 資產，非文字變更，**不需重跑 build_fonts.py**。
- **⚠️ PPTX 繳交版仍是 v5（2026-09-08）**，未含校對輪與 P51 底圖——**需重匯 v6** 才能繳交。
- 專論已定稿可投（OneDrive）；repo 內仍殘留 Word 鎖定檔與作廢舊標題 DOCX（不進 git，可刪）。

## ➡️ 下一步

1. **重匯 PPTX v6**：`cd slides && python build_pptx.py`，成品放
   `C:\Users\phili\OneDrive\文件\演講\2026演講\肥胖醫學會南區研討會\`，命名 `..._v6_<日期>.pptx`，
   v5 作廢。⚠️ 轉檔前先確認伺服器 port（見注意事項的 8765 衝突），並 `curl` 驗證 51 個 `<section>`。
2. 演講日 **2026-09-20**：v6 匯出後剩排練（51 頁配 40 分鐘）。
3. 使用者若再逐頁指正：事實類先調文獻原文核對；語句類套用「專業醫師口吻」原則
   （見記憶 `slide-content-style-rules`）；改完重測佔高＋孤字、重匯 PPTX。

## ⚠️ 注意事項

### 本輪新增（2026-09-09）

- **🩸 port 8765 兩台電腦都會撞**——`Obesity-lecture`（9/13 場）的 `python -m http.server 8765`
  在家用機與醫院機都在跑，預覽畫面會被換成那份簡報。
  醫院機 `.claude/launch.json` 已改 **8770**；家用機曾臨時用 8899。
  轉 PPTX 前先關掉別場伺服器或指定 `SLIDES_URL`，並 `curl` 驗證 51 個 `<section>`。
- 醫院機有一筆已被遠端取代的 stash（舊 P51 修改），無影響，可 `git stash drop`。
- draw 技能輸出目錄為 `slides/generated/`（非 `slides/images/generated/`），已補進 .gitignore。
- **內部查證筆記不上畫面**（使用者鐵律，已存記憶 `slide-content-style-rules`）：
  「已依 reference/xxx 查證」「疑似幻覺已刪除」「請勿於講稿使用」「被追問需說明」類文字
  一律放 HTML 註解或 reference/，不得出現在投影片上。
- **小字兩分法**：純出處列 13px 可；承載觀眾內容的說明要用 quote-box（24.8px）以上；
  標籤 chip 至少 19px。孤字（行末單獨一字）逐頁檢測後才算完工。
- 本輪為文字與版型調整，無新增字元（fontTools 已驗證），**未重跑 build_fonts.py**。

### 既有（未變動）

- **P9 事實底線**：成人肥胖指引 2025〈科技與虛擬醫療〉由講者本人執筆（AI 聊天機器人／CDSS 各 2C）。
  任何「AI 未被指引收錄」的表述都要先核對這份指引。
- 改 `slides/index.html` 內文後原則上重跑 `build_fonts.py`（可先用 fontTools 比對省略）；emoji 不在字型內。
- 版面 90% 佔高上限：改頁後實測 `section.scrollHeight / 720`。
- 離線原則：`slides/index.html` 不得出現 CDN 連結。
- `build_pptx.py` 不可用 `wait_until="networkidle"`（Firebase 長連線必逾時）；
  X108521 沒裝 chromium，一律 `channel="chrome"`（已內建 fallback）。
- GitHub Pages 靜態資源 10 分鐘快取；新圖不可命名 `cover_*.png`（.gitignore 擋）。
- repo 公開：門診數據去識別化、聚合呈現；換診間照片前必讀 `reference/clinic-photo-redaction-20260817.md`。
- 引用外部指引改寫為摘述（講者自己的著作不在此限）。
- 醫院電腦 X108521：外連下載被擋（build_fonts.py 會失敗）、`convert` 非 ImageMagick、
  Playwright 用 chrome channel；office 帳號 Obsidian vault 已有本專案資料夾。
- 專論退修流程：改 `content/article-newsletter-2026.md` → `cd article && python build_docx.py "<檔名>.docx"`；
  勿動 `build_docx.py` 的 `ANCHORS` 句（錨點失配時是去更新 ANCHORS，不是改回內文）。
  文獻一律 NCBI E-utilities 查證（PubMed 網頁版擋 cookie，esummary API 可直取）。
  Word COM 用 `win32com.client.Dispatch`（PowerShell PIA 會拋 TYPE_E_CANTLOADLIBRARY）；
  接上使用者開啟的 Word 實例時**絕不呼叫 `app.Quit()`**。
  Gmail／Drive MCP 傳不了大附件（base64 超上限），寄檔請使用者自己拖曳。

## 🕐 最後更新

- 時間：2026-09-09（醫院場收工）
- 更新者：Claude Code（Fable 5）@ X108521（醫院）
- 階段：P51 底圖定案掛載，**PPTX v6 仍待匯**
- Git push：待推
- L3 Obsidian：待更新
- 前一筆：2026-09-09 @ DESKTOP-LVSV9Q5（家用）· ✅ 已推（`9ef14c8`）
