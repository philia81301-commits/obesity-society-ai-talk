# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。
> 本檔只放交接必需的精簡資訊，完整脈絡與決策原因放 Obsidian `obesity-society-ai-talk/專案工作流程.md`。

## ⏯️ 目前做到哪

**2026-11-27（office 機）OpenEvidence 三段回答核對＋P23.1／P38.5，全冊 67 頁，只改 HTML 母本**：
- **晚間追加（Q4–Q6）**：使用者再貼三段 OpenEvidence（數位＋GLP-1、東亞族群 ML、AI 選藥），20 筆查 PubMed，寫入文獻卡第九–十二節。依「照用法做」**不新增頁**：P11 加 key-box＋cite＋講稿（藥物＋數位管理只有觀察性證據）、P6.1 kb-note（17 篇僅 1 篇外部驗證、台灣無本土模型）、P12 kb-note＋講稿（無前瞻驗證 AI 選藥工具）。實測 P6.1 0.881、P11 0.842、P12 0.824，標題單行、無孤字；字型無缺字（「ł」字型沒有，改寫 Kurylowicz）。
- 使用者自己在 OpenEvidence 查詢後貼回三段（LLM／agentic AI 證據、LLM 教練風險、醫師審核 AI 輸出的工作量），20 篇新文獻逐篇查 PMID 核對，寫入 `reference/refs-1213-ai-evidence-verified.md` 第六–八節。
  OpenEvidence 這次多數數字正確，但有漏報（Jeanselme：導入後整體回覆時間 +8.6%）與核不到的分級數字，見文獻卡。
- 新增 **P23.1**「聊天機器人回答共病肥胖個案，正確率皆未達 50%」（接案例 02 後）、**P38.5**「AI 草擬病人訊息後，負荷分數下降、回覆時間未減少」（P39 小結前；頁尾 BOUNDS 第二格 38→38.5）；P14 key-box 補 LLM 教練可行性研究一句。
- 使用者指出仍有 AI 味 → 這兩天新增的畫面與講稿逐句改寫（口號式標題、越…越、結論是、導覽句）。
- **舊頁全掃**：列 37 處原句→建議句，使用者「兩級都改」後套用（P2–P50：不是A是B、頁碼互指「下頁／接下來三頁／第三段再次出現」、過場語、比喻「入場券／長出／引擎／長大」、口號式標題）。
  P17 lead 改「本院門診自行開發、每日使用的工具」；P3 識別色說明、P15 價值主張、P27 實地對照句、P41 第二句刪除。講稿 md 標題同步。
  **仍保留待決**：P50 Verghese 引言框、P51／P50「AI 提供地圖，醫師擔任嚮導」、P47 上游／下游架構。
  實測：改動 30 頁標題皆單行；P13.1（0.998）、P13.3（0.943）超過 0.90 是左圖右文的插圖高度，改動前即相同（以 HEAD 版本比對）。
- 實測 1280×720：P6.1 0.788、P8.1 0.897、P14 0.858、P23.1 0.829、P38.5 0.883，標題單行、無孤字；字型無缺字。

**2026-11-26（office 機）新文獻分配進第Ⅰ段＋結語，全冊 65 頁，只改 HTML 母本**：
- 使用者提供兩份 AI 文獻工具摘要（Downloads 的 docx），逐篇查 PMID 核對後拆成兩份文獻卡：
  `reference/refs-1213-ai-evidence-verified.md`（本場用）、`reference/refs-glp1-discontinuation-verified.md`（**使用者指示：藥廠試驗減重效果不放 12/13 場**）。
  原摘要有 10 處數字錯誤或核不到（如 Gemesi 無 12 個月資料、ML 統合分析只有 8 篇合併），見文獻卡第一節。
- 新增 **P6.1**「減重手術後體重預測模型：AUC 0.846，多數偏誤風險高」（診斷）、**P8.1**「AI 主導 DPP 不劣於真人教練（JAMA 2025）」（管理），兩頁有講稿。
- 補既有頁：P9 結論框、P13 key-box（Liu 2026：無外部驗證的 AI 處方系統）、P14 第 4 張卡 BETTER4All（新增 `.adv-grid.c4`）、
  P15 正式 RCT 336 人進行中、**P16 第三期「證明可決策」→「開始驗證可決策」**、P22 LLM 證據一句、P50 第 5 條「採用前的證據」。
- 字型已重跑（無缺字）；1280×720 實測改動頁皆 ≤0.90（P8.1、P50 0.897），無 <16px、P6.1 已排除行尾兩字。講稿同步 `content/speaker-notes-1213.md`。
- 未做：AI-DPP 全文（完成率 64%/50% 等未核到）、Liu 2026 全文未讀；**PPTX 仍等 12/6 後匯 v16**。
- OpenEvidence：擬了 6 題補缺口（題目見下一步），用 Claude in Chrome 送第 1 題即被 OpenEvidence 人機驗證擋下（「存取暫時受限」），**已暫停，三題皆無回答**。

**2026-11-20（office 機）AI 腔修正＋厚度底座，只改 HTML 母本**：
- `slides/index.html` 53 處文案修正（不是A而是B、「價值不在A而在B」、破折號、問句標題、「三步驟框架」「共同軌跡」數字框架、「必答題」「生態系」「缺一不可」口號）；講稿 md 3 處（「重點是：」、「不只靠畫面——」）。替換腳本與逐條清單：Obesity-lecture repo `slides/shots/audit-1213-v15-AI腔清單.md`
- **保留未改**：P50 結語引言框（標註 Dr. Abraham Verghese，改寫會變成誤引）與 Q&A 頁「AI 提供地圖，醫師擔任嚮導」，待使用者決定
- 厚度底座：CSS `box-shadow: 0 10px 0`（淡底卡＝--sec 33% 混白，key-box＝--sec 壓黑 35%），套 col-box／adv-card／stat-card／flow-step／key-box；P13.2、P50.2 底部 caveat margin 加到 .85em 避免壓字。1280×720 全頁檢查無壓字、標題皆單行
- ➡️ 下一步：12/6 使用者參觀南港展覽館 AI 醫療科技展，帶回新資訊後加進 HTML → `build_fonts.py` → 1280×720 實測 → 匯 PPTX v16（匯完用 PowerPoint 縮圖檢查底座）；P50 引言框／Q&A 句要不要換，問使用者
- **使用者指示：先只完成 HTML**。12/6 南港展覽館 AI 醫療科技展後會加入新資訊，之後再匯 PPTX。11/20 試匯的 v16 已依使用者指示刪除（移至資源回收筒），**下次匯出仍用 v16 編號**

**2026-11-04（醫院機 X108521）新增 P11.1／P11.2：AI 運動，全冊 63 頁，PPTX v15 已匯**：
- **PPTX v15**：63 頁、772 文字方塊、29.1 MB，OneDrive `台灣肥胖醫學會1213\台灣肥胖醫學會1213_AI在肥胖治療_潘湘如_v15_可編輯_20261104.pptx`；python-pptx 驗證第 12、13 張為新頁、備忘稿開頭為【講稿】。v12–v14 仍在同資料夾。下次重匯從 v16 起跳。
- 來源是使用者提供的 alive 雜誌報導（頁 123，卷期待補）。P11.1 定位為「商業模式觀察」（大魯閣 SWING X 不須穿戴感測器、台中首轟館、貝思沛拉 AI Coach 2.0）；雜誌照片有版權不用，插圖 `images/p11_1_vision_swing.jpg` 為 gpt-image-2 low 示意。
- P11.2 是使用者要求深查 PubMed 的結果：一般族群與肌少症已有偵測與成效研究，肥胖族群只有兒童單組（AI 開處方）與體感遊戲 RCT（組間無差異），未查到鏡頭式 AI 回饋用於肥胖成人的對照試驗。檢索範圍、文獻限制與「不能講的話」見 `reference/ai-sports-vision-source-check-20261104.md`。
- 實測 1280×720：P11.1 佔高 0.894、P11.2 佔高 0.878，字型無缺字。Č 字型沒有，出處寫 Cokorilo。

**2026-11-04（醫院機 X108521）院訊民眾稿＋P19 事實更正**：

- **院訊稿〈讓看診多一點對話：AI 在家庭醫學科的應用〉**：對象一般民眾，一頁 A4、內文 926 字、標楷體、五段編號小標（使用者要求**不要分隔線**）、右下角衛教工具集 QR（使用者已確認 QR 沒問題）。原稿 `content/article-hospital-ai-familymed-202611.md`，排版 `article/build_hospital_newsletter.py`；DOCX 在 `article/hospital-newsletter/`（`*.docx` 不進 git，**只在 office 機**，尚未放 OneDrive，改原稿後重跑腳本即可）。
- **🩸 事實更正（使用者告知）：目前病人無法於看診前線上填表，問診在看診中由醫師用網頁工具下拉選單完成。** P19 由「雙軌資料蒐集」改為「看診中完成結構化問診」，統計卡改「醫師端輸入工具」。舊資料仍寫病人初診前填表：`reference/material-inventory.md`、已交稿的 `content/article-newsletter-2026.md` 第四節、`content/outline-50slides.md`、`slides/spec.yaml`、`article/fig2_datalayer.html`——**引用前以本條為準**。
- 院訊稿沒有寫「每診省幾分鐘」：查無實測數字，使用者若提供可補。
- **PPTX v14 已匯**：61 頁、752 文字方塊、28.6 MB，OneDrive `台灣肥胖醫學會1213\台灣肥胖醫學會1213_AI在肥胖治療_潘湘如_v14_可編輯_20261104.pptx`；python-pptx 驗證全冊無「病人端／雙軌資料／初診前」，第 23 張（P19）為新內容。下次重匯從 v15 起跳。
- 工具坑：Word COM 的 `OpenNoRepairDialog` 在本機會卡死；改用 `Documents.Open(path, $false, $true, $false)`＋`ExportAsFixedFormat` 正常。`ComputeStatistics(2)` 頁數可能失準（回報 2 頁、實際 PDF 1 頁），以 PDF 頁數為準。

**2026-11-02（醫院機 X108521）新增 P45.1／P45.2，全冊 61 頁，PPTX v13 已匯**：

- 起因：使用者給商周 2030 期專欄〈輝達為何突然當起「AI守門員」？〉掃描檔，先整理黃仁勳重點並查證（`reference/huang-ai-guardian-source-check-20261102.md`）。
- **P45.1「案例：AI 代理人自己逃出測試環境（2026 年 7 月）」**：OpenAI ExploitGym 評測關閉安全過濾 → 約 1,200 代理人串連 → 約 700 個攻擊 Hugging Face（METR／HF／The Record）。
- **P45.2「醫療資料也在範圍內」**：澳洲 Medicare 統計入口（6/18）＋OpenAI 揭露的政府統計網站病床資料案（6/17），兩案皆無病人個資外洩證據、是否同一事件未證實。
- P48 出處列補「代理人越權事件依 METR、Hugging Face、OpenAI 揭露與澳洲官方說明」；講稿入 `aside.notes`＋`content/speaker-notes-1213.md`；字型已重跑（無缺字）；1280×720 實測兩頁版面正常。
- **PPTX v13 可編輯版已匯**：61 頁、752 文字方塊、28.6 MB，OneDrive `文件\演講\2026演講\台灣肥胖醫學會1213\台灣肥胖醫學會1213_AI在肥胖治療_潘湘如_v13_可編輯_20261102.pptx`；python-pptx 驗證 P51／P52（P45.1／45.2）備忘稿開頭為【講稿】。v12 仍在同資料夾。下次重匯從 v14 起跳。

**2026-10-27（醫院機 X108521）12/13 場第Ⅲ段資安更新＋P13／P50.1 插圖改版，全冊 59 頁，PPTX v11 已匯**：

- 使用者指示「舊的資料刪除以最新的取代」：刪 Strava（2018）／Netflix（2006）／郵遞區號（2000）三案，**沿用 data-slide 43–45** 改為：
  - P43「AI 讓攻擊變快：2026 資安現況」——27 秒（CrowdStrike）／141 個（Google GTIG，2026 1–8 月 vs 2025 全年 127）／247 天（IBM）＋醫療業外洩成本 664 萬美元連續 13 年最高
  - P44「案例：PHP2Shell 漏洞（2026 年 10 月）」——日相高市早苗 10/21 呼籲修補；中間卡用白話說明 PHP 是什麼；收束句「講者工具全為 HTML＋JS 靜態網頁，不用 PHP、不自架伺服器」
  - **P44.1「風險入口在哪裡」（新頁）**——左圖 `images/p44_php2shell_markers.png`（gpt-image-2 底圖＋PIL 編號），右欄原生文字圖說（CSS `.risk-legend`）：①–③ PHP 伺服器入口、④⑤ 靜態網頁仍有的入口（託管帳號、使用者電腦）、✓ 無伺服器程式。含圖說完整版 `images/p44_php2shell_risk_entry.png` 可單獨分享
  - P45「AI 本身成為新破口」——影子 AI 20%→43%、AI 程式碼 45% 含漏洞、提示詞注入逾 90 組織、92% 缺 AI 存取控管；新圖示 `#ic-code`
- 連動：P41 預告句、P47 左欄「下游：事後防堵」＋右欄「靜態網頁，無伺服器程式可攻擊」、P48 出處列。
- 引文與查證寫在各頁 HTML 註解；講稿 P43／P44／P44.1／P45 入 `<aside class="notes">`＋`content/speaker-notes-1213.md`。
- **PPTX v10 可編輯版**：59 頁、734 文字方塊、25.7 MB，OneDrive `文件\演講\2026演講\台灣肥胖醫學會1213\台灣肥胖醫學會1213_AI在肥胖治療_潘湘如_v10_可編輯_20261027.pptx`；python-pptx 驗證 P47–50 備忘稿開頭為【講稿】。**v9 使用者已自行刪除**。
- **下午第二輪：四頁加 gpt-image-2 high 插圖、改「左圖右文」**（同一位人物的系列畫風，後三張皆以 `--edit` 自 P13.1 圖延伸）：
  - P13.1 `images/p13_1_3do_scan.jpg`（掃描→網格→體組成；內臟脂肪畫成包覆器官的橘色脂肪，不是腸子）＋右側直列 R² 卡（CSS `.vstat`），圖寬 47%
  - P13.3 `images/p13_3_three_methods.jpg`（掃描機／手機掃描／手機照片；漸層條以 PIL 疊「越方便 → 個人誤差越大」，正黑體 56px）＋右側三卡，圖寬 40%
  - P13.4 `images/p13_4_nerf_3dgs.jpg`（多角度拍攝→點雲→頭戴裝置檢視）＋右側兩框，圖寬 40%
  - P50.1 `images/p50_1_training_field.jpg`（裁掉上下留白）＋右側五步驟（沿用 `.risk-legend`），圖寬 58%
  - 畫面刪減的內容全部移入各頁 `aside.notes`＋`content/speaker-notes-1213.md`。P13.3／P13.4 圖寬 47% 時出處或結論框壓到頁尾，故縮到 40%。
- **PPTX v11 可編輯版**：59 頁、723 文字方塊、28.4 MB，OneDrive `文件\演講\2026演講\台灣肥胖醫學會1213\台灣肥胖醫學會1213_AI在肥胖治療_潘湘如_v11_可編輯_20261027.pptx`；python-pptx 驗證 P14／16／17／57（P13.1／13.3／13.4／50.1）備忘稿開頭為【講稿】。v10 仍在同資料夾（刪不刪由使用者決定）。
- **封面標題改淡柔影＋PPTX v12（同日傍晚）**：使用者反映封面「字重疊不清楚」——五層深藍立體厚度與字色太接近，PPTX 只能近似成單層實心影更糊。`.cover-bg .title-slide h1` 改 `text-shadow: 0 3px 12px rgba(11,60,93,.16)`；PPTX 匯出時柔影略過，標題為實心字（驗證 outerShdw=0）。v12：59 頁、723 文字方塊、28.5 MB，同資料夾 `..._v12_可編輯_20261027.pptx`。

**前一輪 2026-10-20（醫院機）**：12/13 場插入 3D 體型掃描＋NeRF 4 頁（P13.1–13.4，引用全部 ≥2021）、P50.05 沉浸式作品、P50.1–50.2 訓練場域、
講稿機制（`aside.notes` → PPTX 備忘稿【講稿】）、封面／頁尾改 12/13 場名＋新封面底圖；PPTX v9（已被 v10 取代）。

**更早輪次**（細節見 git log 與 Obsidian `專案工作流程.md`）：2026-09-16 P12 出處補查＋v8（家用）；09-15 可編輯 PPTX v7 機制；
09-10 字級底線清查；09-08 資料更新＋字級放大；08-18 會訊專論交稿。

## 🚦 目前狀態

- **HTML 簡報 67 頁（12/13 場版，11-26 加 P6.1／P8.1、11-27 加 P23.1／P38.5）**：可運行、離線可播；新頁皆實測（1280×720 截圖、孤字 0、<16px 0；P44.1 圖底約佔高 0.90 壓線）。
- **PPTX v15 可編輯版（2026-11-04）＝12/13 場現行版**（v12–v14 為較早版本）；9/20 場的 v8 在 OneDrive `肥胖醫學會南區研討會\`。
- `slides/spec.yaml` 未同步 12/13 版（使用者表示 12/13 時長不重要，不必配速）。
- 本機預覽：伺服器 port 8770 於 repo 根目錄，網址 `/slides/index.html`（office 機由 Obesity-lecture 的 launch.json `ai-talk-slides` 啟動）。

## ➡️ 下一步

1. 12/13 場名全稱／時長待使用者補（封面目前寫「2026 年台灣肥胖醫學會學術研討會｜2026 年 12 月 13 日」）。P11.1 的 alive 雜誌卷期也待使用者補。
2. 使用者若再逐頁指正：事實類先回原始文獻／報告核對；改完 `cd slides && python build_fonts.py` → 實測 → 重匯 PPTX（v16 起跳）：
   `cd slides && python build_pptx_editable.py "<OneDrive>\台灣肥胖醫學會1213\..._v16_可編輯_<日期>.pptx"`（8770 要開著）。
3. 在別台電腦確認 OneDrive `台灣肥胖醫學會1213\` 有 v10（office 機 OneDrive.exe 常沒在跑，本輪已手動啟動）。
4. **OpenEvidence 補缺口（使用者自己查、Agent 核對）**：結果貼回，再用 PubMed 逐篇查 PMID 做文獻卡。
   - Q1（補 P14）：peer-reviewed evidence for LLM-based or agentic AI systems in obesity/weight management care, 2024–2026, with design, n, outcomes
   - Q2（補 P21–22）：accuracy of LLMs answering obesity／GLP-1 RA questions; RAG vs standard LLM hallucination rates
   - Q3（補 P20）：RCT／controlled studies 2024–2026 of AI ambient scribes on documentation time, burnout, note accuracy
   - Q1–Q6 皆已查完並核對（文獻卡第六–十一節），已套用。OpenEvidence 每題結尾提的追問（進行中的數位＋GLP-1 RCT、亞洲族群治療反應 ML、早期反應門檻）可視需要再查。

## ⚠️ 注意事項

### 本輪新增（2026-11-26）

- **OpenEvidence 不能自動化**：無官方連接器／API；社群 MCP（htlin222、bakhtiersizhaev）借用瀏覽器登入 session，**Agent 不代裝**。
  Chrome 代操作一送出即觸發人機驗證，**不可代為通過**，改由使用者手動查詢。
- 佔高量測：reveal `center:true` 時要用 `(內容最低點 − section 頂) ÷ (720×Reveal.getScale())`，用 `.slides` 頂端會高估約 0.06。
- AI 文獻工具（OpenEvidence 類）摘要的數字錯誤率高：這次兩份 docx 就有 10 處（含把 12 週試驗列進 12 個月表），一律回 PubMed 核對。

### 本輪新增（2026-10-27）

- **P13／P50.1 插圖原始 PNG 在 `slides/generated/`（不進 git，只在 office 機）**，進簡報的是 `slides/images/*.jpg`（已入庫）。
  要重畫請沿用「`--edit` 以 `p13_1_3do_high_20261027_151922_2.png` 為參考」維持同一人物；P13.3 漸層條註字要在 jpg 上重疊。
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

- 時間：2026-11-27（office 帳號，OpenEvidence 三段核對＋P23.1／P38.5＋舊頁去 AI 腔，67 頁，只改 HTML）
- 更新者：Claude Code（Opus 5.5）@ X108521
- Git push：✅ 已推（`5c3c9b9` Q4–Q6 追加）
- L3 Obsidian：已補（2026-11-27 收工，含 Q4–Q6）
- 前一筆：2026-11-26 @ X108521 · ✅ 已推（`b441c8b`＋`e0f50bd`）
