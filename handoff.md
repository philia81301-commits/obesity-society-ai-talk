# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。
> 本檔只放交接必需的精簡資訊，完整脈絡與決策原因放 Obsidian `obesity-society-ai-talk/專案工作流程.md`。

## ⏯️ 目前做到哪

**2026-09-08（醫院電腦 X108521，office 帳號）第三輪（收工）**：P6 事實修正＋錯字修正，**PPTX v5 已匯出（現行版）**。

- **P6 依原文（PMID 34335479，Lin Z, Front Endocrinol 2021;12:713592）逐項修正**：
  n 2,945→**2,495**（主分群隊列上海 882 名肥胖患者）；**HMO-I 原誤標「合併 PCOS／糖尿病」
  →高胰島素型（PCOS 風險高）**，糖尿病風險最高者實為 **LMO**（圖例對調）；
  引註頁碼原混到 P5 那篇 Endocrine 2022（12:63–72）→ 12:713592。
- **P6 標尺錯字**：「帶代謝異常 56%」→「**代謝異常 56%**」（使用者連續兩次指正的就是這個「帶」字，
  與左側「代謝健康 44%」對仗）。圖例全部收一行不折句，佔高 0.846。
- **PPTX v5**：`肥胖醫學會南區研討會_AI在肥胖治療_潘湘如_v5_20260908.pptx`（51 頁、28.1 MB），
  office 端 OneDrive 演講資料夾。**v1–v4 全數作廢，繳交認明 v5**。

**2026-09-08（醫院電腦 X108521，office 帳號）第二輪**：全簡報字級放大＋P23 待補區塊移除，PPTX v4 已匯出（已被 v5 取代）。

- **base 42→46px**（依使用者字級原則記憶 `slide-typography-rules`：base ≥23px@720 等效、
  與 9/13 場 21→23px 同幅度）；`.cmp-cap` .34→.36em 補過「註記 ≥16px」門檻。
- **出處列 `.cite` 改固定 13px** 不隨 base 放大（記憶允許出處 12–13px）——P6/P9/P10/P27 靠這行救回。
- 空隙壓縮：`.col-box` padding 18→15、`.flow-step` 16→12、`.quote-box` 16→12、
  診間照片 `fs-photo` 138→120px、P20 截圖 215→184px、P2 文字雲框 114→92px、
  P9 key-box 局部 .5em。**全 51 頁實測佔高 ≤0.90**（最高 P25／P50 0.897）。
- **P23「待補敏感議題判定範圍」區塊依使用者指示整塊移除**，不再補件——階段七就此結案。
- 字級調整無新增字元，**免跑 build_fonts.py**。
- **PPTX v4**：`肥胖醫學會南區研討會_AI在肥胖治療_潘湘如_v4_20260908.pptx`（51 頁、26.5 MB），
  同資料夾的 v3（當日稍早）與 v1/v2 皆作廢，**繳交認明 v4**。

**2026-09-08（醫院電腦 X108521，office 帳號）第一輪**：投影片資料更新兩處＋PPTX v3 重匯。

- **P25 截圖換成 2026-08 月報**（新圖 `slides/images/p25_report_charts_202608.png`，
  由 weight-clinic-reports 的 2026-08.html 以 Playwright 2 倍截取；caption 同步改 2026-08）。
- **P20 新增一條 bullet**：「維持期追蹤表單已於 2026-08 上線」（Google Drive 上 8/18 建立的
  「\*體重維持紀錄」表單工具，資料持續累積中）。加字後超過 90% 佔高，
  該頁截圖以 inline style 壓至 `max-height:215px`，實測 0.887／P25 為 0.853。
- 新增文字經 fontTools 檢查**字型子集無缺字**，不需重跑 build_fonts.py（醫院電腦也跑不了）。
- **PPTX v3 已匯出**：`肥胖醫學會南區研討會_AI在肥胖治療_潘湘如_v3_20260908.pptx`
  （51 頁、28.6 MB），在 **office 這台的 OneDrive**
  `C:\Users\office\OneDrive\文件\演講\2026演講\肥胖醫學會南區研討會\`（與 phili 家用機同一雲端資料夾）。
  ⚠️ 醫院 `D:\潘湘如\演講\2026演講\肥胖醫學會南區研討會\` **不是**同步中的那份（只有 8/14 摘要），別存那裡。
- 另查證：WHO 首份 GLP-1 肥胖指引（2025-12）全文 0 次提到 AI/ML——可作 P9 口頭補充素材，未動版面。

**2026-08-18（家用電腦 DESKTOP-LVSV9Q5）**：本次**沒有動投影片**，全部工時在新增的
**階段八——肥胖醫學會會訊醫學專論**。當日交稿、當日完成。

- **新產出一篇專論**《人工智慧在肥胖治療的臨床定位：證據等級、門診落地與治理界線》，
  12 頁、正文 4,198 字、4 圖 2 表、14 條引註、4 題自我評量附解析。
- 體例逐項比照使用者前一篇〈體重管理的數位轉型〉（Word COM 轉檔後實測版面值）。
- 原始稿 `content/article-newsletter-2026.md` 為**單一真實來源**，
  DOCX 由 `article/build_docx.py` 產生，成品存 OneDrive、不進 git。

## 🚦 目前狀態

- **專論已定稿可投**。DOCX 與 PDF 都在
  `C:\Users\phili\OneDrive\文件\演講\2026演講\肥胖醫學會南區研討會\`。
- **14 條參考文獻全部經 NCBI E-utilities 逐筆核對**，作者與卷頁皆可查。
- **投影片（51 頁）已定版**：可運行、離線可播、內容缺口全數結案，PPTX v5 為繳交版；剩排練。
- ⚠️ **repo 內殘留 Word 鎖定檔** `article/~$…docx`（使用者當時開著舊檔）。
  不進 git（`.gitignore` 擋 `*.docx`），但關掉 Word 後可自行刪除。
- ⚠️ repo 內另有一份**作廢的舊標題 DOCX**（`…運用的新發展…`），同樣不進 git，可刪。

## ➡️ 下一步

1. ~~P23 敏感議題判定範圍~~ **2026-09-08 使用者指示整塊移除，不再補件——內容缺口全數結案**。
2. 演講日 2026-09-20，剩餘工作只剩**排練**（51 頁配 40 分鐘）；PPTX 繳交認明 **v5**。
   使用者本輪正逐頁校對（S6 已改）——**若再收到「S<n> 有錯」類指正，優先調文獻原文核對**，
   不要只改字面；改完重測佔高、重匯 PPTX。
3. **專論若被編輯退修**：改 `content/article-newsletter-2026.md`，
   然後 `cd article && python build_docx.py "<輸出檔名>.docx"`。
   ⚠️ 改內文時注意別動到 `build_docx.py` 的 `ANCHORS` 句子（見下）。

## ⚠️ 注意事項

### 本次新增（階段八）

- **🩸 `build_docx.py` 的圖表錨點會被潤稿咬到**——圖表插入點是靠「內文包含某句話」定位。
  本次修語氣時改掉了兩句，害**圖二與表二靜靜消失**、產出一份少圖的 DOCX 卻沒有任何錯誤訊息。
  已加防呆：`build()` 結尾檢查所有錨點是否命中，沒命中直接 `SystemExit`。
  **改內文後若程式報「錨點失配」，是去更新 `ANCHORS` 的字串，不是改回內文。**
- **🔴 文獻不能憑印象填**——原本 5 條文獻缺作者，用 NCBI E-utilities 查完發現**兩條是錯的**：
  - `[3]` 原標「J Endocr Soc 2025 會議摘要」，實為 **Adv Ther 2025;42:5010–22 期刊全文**
    （Toliver JC 等，PMID 40768192）。等於把同儕審查論文降格成摘要。
  - `[2]`、`[7]` 的**篇名是依內容描述自行填的，不是真實標題**，已換成 PubMed 原題。
  → **PubMed 網頁版擋 cookie，WebFetch 讀不到**；改用
    `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=<PMID>&retmode=json` 可直接取。
- **圖二不可用實際操作截圖**（2026-08-18 使用者指示）——原截圖把欄位配置與病歷貼稿樣板整套曝光，
  怕被照抄，已改為概念圖 `article/fig2_datalayer.html`。順帶解決了原截圖的
  BMI 30.5 卻勾選 27-30、以及出現 Ozempic 商品名兩個問題。
- **Word COM 在這台會拋 TYPE_E_CANTLOADLIBRARY**——PowerShell 的 `New-Object -ComObject Word.Application`
  會因 PIA 轉型失敗。**改用 Python `win32com.client.Dispatch` 就正常**（晚期繫結）。
  舊 `.doc` 也可用 `antiword -m UTF-8.txt` 取文字。
- **⚠️ Word COM 會接上使用者已開啟的那個 Word 實例**——此時**絕對不要呼叫 `app.Quit()`**，
  會把使用者正在看的文件一起關掉。只 `d.Close(False)` 關自己開的那份即可。
- **Gmail／Google Drive MCP 無法傳大附件**——兩者都要求 base64 字串塞進參數，
  2 MB 的 DOCX 轉出來約 280 萬字元，遠超單次工具呼叫上限。**寄檔案請使用者自己從資料夾拖曳。**
- **中文字數統計**：正文（摘要～結論）4,198 字，比原訂 3,000–3,500 多約 700。
  2026-08-18 使用者明確指示「**不用砍**」，是刻意保留的，不是漏改。

### 既有（投影片相關，未變動）

- ~~P23 的線索已斷~~ **2026-09-08 結案**：使用者指示整塊移除待補區塊，不再需要該出處。
- **P9 的事實修正（最重要）**：`成人肥胖指引 2025〈科技與虛擬醫療在體重管理的運用〉`
  **由講者本人執筆**，含 6 條 GRADE 建議，AI 聊天機器人與 CDSS 各一條（皆 2C）。
  **日後任何「AI 未被指引收錄」的表述都要先核對這份指引。**
- **改 `slides/index.html` 內文後原則上要重跑 `build_fonts.py`**（可用 fontTools 比對現有子集省略）。
  ⚠️ **emoji 不在 Noto Sans TC 裡**。
- **版面 90% 佔高上限**：改完頁面要實測 `section.scrollHeight / 720`。
- **離線原則**：`slides/index.html` 內不得出現任何 CDN 連結。
- **`build_pptx.py` 不可用 `wait_until="networkidle"`**——Firebase 長連線會讓它必定逾時。
- **GitHub Pages 靜態資源有 10 分鐘快取**（`max-age=600`），剛 push 完看到舊版是本機快取。
- **圖檔命名**：新圖不可叫 `cover_*.png`（`.gitignore` 擋掉該樣式）。
- repo 為公開：門診數據一律去識別化、聚合呈現；原始資料檔不進 git。
  **門診實拍的去識別化紀錄見 `reference/clinic-photo-redaction-20260817.md`，換照片前必讀。**
- 引用外部指引時**改寫為摘述、不整段逐字轉錄**（講者自己的著作不在此限）。
- **醫院電腦 X108521 的限制**：網路擋外連下載（`build_fonts.py` 會失敗）、
  `convert` 是 Windows 磁碟工具不是 ImageMagick。
  ~~Obsidian vault 在 office 帳號下無本專案資料夾~~ **2026-09-08 已存在**
  （`C:\Users\office\OneDrive\2ndBrain\obesity-society-ai-talk\`，L3 可直接檔案編輯）。
- **🩸 X108521 的 port 8765 會被另一專案佔用**——`C:\projects\Obesity-lecture\`（9/13、9/15 兩場演講）
  也慣用 `python -m http.server 8765`，且 Windows 允許兩個行程同綁一個 port、**連線落在先啟動的那個**。
  2026-09-08 因此把別場的 59 頁簡報轉成本場 PPTX 而不自知（已刪除重做）。
  `build_pptx.py` 現支援 `SLIDES_URL` 環境變數改 port；轉檔前先
  `curl http://127.0.0.1:<port>/slides/index.html | grep -c "<section"` 確認是 51。
- Playwright 在 X108521 沒裝 chromium（下載被擋），**一律用 `channel="chrome"`**（build_pptx.py 已內建 fallback）。

## 🕐 最後更新

- 時間：2026-09-08（第三輪，收工）
- 更新者：Claude Code（Fable 5）@ X108521（醫院，office 帳號）
- 階段：**階段七結案**；字級放大、資料更新至 2026-08、P6 事實修正完成，**PPTX v5 為現行繳交版**
- Git push：✅ 已推（`830eab8`）
- L3 Obsidian：✅ 已更新（office 端 vault 已有本專案資料夾；補「2026-09-08 的決策與踩坑」與更動紀錄一列）
- 前一筆：2026-08-18 @ DESKTOP-LVSV9Q5（家用）· ✅ 已推（`efedcf9`）
