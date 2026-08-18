# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。
> 本檔只放交接必需的精簡資訊，完整脈絡與決策原因放 Obsidian `obesity-society-ai-talk/專案工作流程.md`。

## ⏯️ 目前做到哪

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
- **投影片（51 頁）狀態未變**：可運行，離線可播，剩 P23 一項內容待補。
- ⚠️ **repo 內殘留 Word 鎖定檔** `article/~$…docx`（使用者當時開著舊檔）。
  不進 git（`.gitignore` 擋 `*.docx`），但關掉 Word 後可自行刪除。
- ⚠️ repo 內另有一份**作廢的舊標題 DOCX**（`…運用的新發展…`），同樣不進 git，可刪。

## ➡️ 下一步

1. **投影片的 P23 敏感議題判定範圍**仍是唯一缺口（線索已斷，見下方注意事項）。
   補完後要重跑一次 PPTX。
2. **專論若被編輯退修**：改 `content/article-newsletter-2026.md`，
   然後 `cd article && python build_docx.py "<輸出檔名>.docx"`。
   ⚠️ 改內文時注意別動到 `build_docx.py` 的 `ANCHORS` 句子（見下）。
3. 演講日 2026-09-20，剩餘工作以排練與 P23 為主。

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

- **P23 的線索已斷**：出處為 `減重門診AI管理.pptx` 第 9 張投影片備註，
  2026-08-17 在醫院電腦 X108521 上仍未找到，需使用者自行定位或直接口述。
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
  `convert` 是 Windows 磁碟工具不是 ImageMagick、Obsidian vault 在 `office` 帳號下無本專案資料夾。

## 🕐 最後更新

- 時間：2026-08-18
- 更新者：Claude Code（Opus 5）@ DESKTOP-LVSV9Q5（家用）
- 階段：**階段八完成（會訊專論當日交稿）**；階段七仍剩 P23 一項
- Git push：待推（L2 完成後回填）
- L3 Obsidian：待確認本機 MCP 是否可用
- 前一筆：2026-08-17 @ X108521（醫院）· ✅ 已推（`9ef23a0`、`459db86`）
