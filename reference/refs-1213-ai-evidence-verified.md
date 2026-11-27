# 文獻卡：AI 在肥胖管理的證據（12/13 場）

- 建檔：2026-11-26（醫院機）
- 來源：使用者提供的兩份 AI 文獻工具摘要（`Downloads\No validated strategy prevents weight regain after stopping GLP.docx`、`Downloads\AI in obesity management is promising but not yet validated for routine clinical decision.docx`）
- 核對方式：每篇以 DOI 查 PubMed 取得 PMID，數字逐一對照 PubMed 摘要；有 PMC 全文者另外查全文。
- 核對程度標記：**全文**＝PMC 全文核對；**摘要**＝僅 PubMed 摘要；**未核到原文**＝摘要和可取得的全文都找不到該數字，**不得放上投影片**。

- 同批另一份（GLP-1 停藥後體重回升）拆到 `refs-glp1-discontinuation-verified.md`，12/13 場不使用

---

## 一、原稿需要更正的地方

| # | 原稿寫法 | 核對結果 | 處理 |
|---|---------|---------|------|
| 3 | 減重手術 ML 統合分析「12 篇、13,640 人、pooled AUC 0.846」 | 收 12 篇，**合併 AUC 的只有 8 篇**；13,640 人不在摘要 | 改寫為「8 篇合併」，人數不用 |
| 4 | 德國 app 試驗（Gemesi 2024）列在「12 個月結果」表、「ITT 7.8%」 | 該 RCT 只有 **12 週介入＋12 週追蹤**，完成者減 3.2 kg（3.2%）vs 0.4 kg；7.8% 不在本篇 | 移出 12 個月表；7.8% 不用 |
| 5 | DEMETRA 列在「12 個月結果」表 | 主要終點是 **6 個月** | 標 6 個月 |
| 6 | SureMediks「13.7%」 | 摘要寫平均 14%（範圍 4–22%），n=391，無對照的 field trial | 用 14%，並註明無對照 |
| 7 | AI-DPP 完成率 64% vs 50%、七成大學以上學歷、拉丁裔／亞裔／原住民 <10% | PMC 不提供 JAMA 全文；摘要只有開始參加率 93.4% vs 82.7%、Hispanic 6% | 未核到原文 |
| 8 | 減重手術：小型模型 AUC 0.68（n=118）、ESG 模型 AUC 0.88 | Foula 摘要沒有這些數字（88 篇的系統性回顧） | 未核到原文 |
| 9 | 國際專家共識「76% 同意 AI 可預測併發症」 | Kermansaravi 摘要只寫 28 條陳述全部達 ≥70% 共識 | 未核到原文 |
| 10 | Cochrane「多數試驗高偏誤風險」 | 摘要沒有這句 | 未核到原文 |

---

## 二、AI 在肥胖管理的證據

### A1　Liu 2026：AI 在肥胖管理的結構化敘述性回顧（原稿的主要依據）
- Liu W, et al. Artificial intelligence in obesity management: clinical evidence, translational gaps, and implementation priorities—a structured narrative review. *Front Endocrinol (Lausanne).* 2026;17:1955223. doi:10.3389/fendo.2026.1955223
- **PMID 42755727**（PMC13581758）｜SANRA 架構的敘述性回顧，檢索至 2026-06-01
- 結論（摘要，可直接改寫引用）：
  - 明確以 AI 介入、以病人為單位的證據有限且異質
  - 體重成效最好的證據來自多元件數位／混合照護計畫，這些研究**沒有單獨評估 AI 元件**，不能解讀為 AI 本身的療效
  - AI 輔助藥物研發仍在臨床前；以 NLP 分析 GLP-1 RA 不良事件敘述可做訊號偵測，不能做因果推論
  - 表型分型與 ML 輔助基因風險分數可能有助於區分反應者，但**沒有一個經外部驗證、前瞻實施的 AI 處方系統證明改善病人結果**
  - 減重手術的 AI 研究多為回溯或僅內部驗證，很少評估校準、行動閾值與前瞻性影響
  - LLM 可協助衛教與草擬文件，證據不支持在無人監督下選擇治療或術式
  - 臨床採用前需要：獨立外部驗證、前瞻性流程評估、以病人為中心的結果、安全與公平、資料治理、成本效益
- 核對：**摘要**（PMC 有全文，本輪未讀）

### A2　Mathioudakis 2025：AI 主導 DPP vs 真人教練 DPP（JAMA RCT）
- Mathioudakis N, et al. An AI-Powered Lifestyle Intervention vs Human Coaching in the Diabetes Prevention Program: A Randomized Clinical Trial. *JAMA.* 2025;334(23):2079-2089. doi:10.1001/jama.2025.19563
- **PMID 41144242**｜第 3 期、實用性、不劣性 RCT，美國 2 個院區（Baltimore、Reading），n=368，前期糖尿病＋過重／肥胖；NCT05056376
- 數字（摘要）：
  - 收案者中位年齡 58 歲、女性 71%、黑人 27%、Hispanic 6%、白人 61%、中位 BMI 32.3
  - 開始參加：AI 93.4%（171/183）vs 真人 82.7%（153/185）
  - 12 個月複合主要結果：31.7% vs 31.9%（風險差 −0.2%，單尾 95% CI 下限 −8.2%），達不劣性（界限 −15%）
  - 複合結果＝HbA1c 全程 <6.5%，且達成以下任一：體重減 ≥5%；減 ≥4%＋每週 ≥150 分鐘活動；HbA1c 絕對下降 ≥0.2 個百分點
- 解讀：結論是 AI 版**不劣於**真人教練，不是優於一般照護；複合終點含 HbA1c 下降 0.2，不等於 ≥5% 減重
- 未核到原文：完成率 64% vs 50%、學歷分布、各組平均體重變化（PMC 不提供 JAMA 全文）
- 核對：**摘要**
- 相關評論：Kanaya AM, Gadgil MD. ACP Journal Club. *Ann Intern Med.* 2026;179(3):JC34. doi:10.7326/ANNALS-26-00289-JC｜**PMID 41771128**

### A3　Forman 2023：強化學習分配行為減重介入（試驗計畫書）
- Forman EM, et al. Using artificial intelligence to optimize delivery of weight loss treatment: Protocol for an efficacy and cost-effectiveness trial. *Contemp Clin Trials.* 2023;124:107029. doi:10.1016/j.cct.2022.107029
- **PMID 36435427**｜計畫書；N=336，12 個月不劣性 RCT
- 數字（摘要）：先導試驗中 AI 組的教練接觸量約為標準組的三分之一，減重幾乎相同
- 正式試驗結果：**尚未發表**（本輪未另查）
- 核對：**摘要**

### A4　BETTER4All（AI＋多基因風險分數個人化介入，計畫書）
- Karaglani E, et al. AI-Driven Personalized Recommendations and Real-Time Monitoring for the Prevention and Management of Obesity: Clinical Trial Protocol for the Multicentre BETTER4All Personalized Intervention. *Obes Rev.* 2026:e70243. doi:10.1111/obr.70243
- **PMID 42945991**｜多中心 RCT 計畫書，歐洲 7 國，目標 1,022 名 BMI ≥25 成人；NCT06997510
- 設計（摘要）：介入組＝AI＋PRS 建議（app、穿戴裝置、結構化諮詢）；對照組＝標準低熱量飲食建議；主要終點 6 個月 BMI 變化，次要終點含 1 年體重維持
- 結果：**尚未發表**
- 核對：**摘要**

### A5　SureMediks（AI 數位生活型態平台，無對照）
- Khokhar S, et al. Weight Loss with an AI-Powered Digital Platform for Lifestyle Intervention. *Obes Surg.* 2024;34(5):1810-1818. doi:10.1007/s11695-024-07209-1
- **PMID 38573389**｜多國 field trial，無對照組，n=391，24 週
- 數字（摘要）：平均減 14%（範圍 4–22%）；98.7% 減 ≥5%
- 限制：無對照、無 12 個月資料；「所有人都減重」的結果本身就提示選樣或報告偏誤，投影片上不宜當亮點
- 核對：**摘要**

### A6　Chew 2021：AI 用於成人減重的範疇回顧
- Chew HSJ, Ang WHD, Lau Y. The potential of artificial intelligence in enhancing adult weight loss: a scoping review. *Public Health Nutr.* 2021;24(8):1993-2020. doi:10.1017/S1368980021000598
- **PMID 33592164**｜scoping review，66 篇
- 數字（摘要）：機器感知 50 篇、僅預測分析 6 篇、即時分析＋個人化微介入 10 篇；只有 6 篇報告平均減重（2.4–4.7%），其中 2 篇達統計顯著
- 核對：**摘要**（注意 2021 年，檢索至 2020-12）

### A7　Haghighathoseini 2026：AI 用於肥胖預防的系統性回顧
- Haghighathoseini A, et al. A Systematic Review on Applications of Artificial Intelligence for Obesity Prevention. *Obes Rev.* 2026;27(5):e70062. doi:10.1111/obr.70062
- **PMID 41436079**｜系統性回顧，46 篇（2008–2024）
- 內容（摘要）：2018 年後研究量明顯增加；多數集中在肥胖偵測，預防、管理與治療的研究較少；缺乏真實世界整合框架
- 核對：**摘要**

### A8　Wang 2026：減重手術後體重結果的 ML 預測模型統合分析
- Wang J, et al. Machine Learning Prediction Models for Weight Loss Outcomes after Metabolic and Bariatric Surgery: a Systematic Review and Meta-Analysis. *Obes Surg.* 2026;36(6):3301-3311. doi:10.1007/s11695-026-08686-2
- **PMID 42012596**｜SR／MA，收 12 篇，**8 篇**進入合併
- 數字（摘要）：pooled AUC 0.846（95% CI 0.755–0.908），I²=75.4%；PROBAST+AI 評估多數為高偏誤風險（尤其分析面）；TRIPOD+AI 報告遵循度不佳
- 核對：**摘要**

### A9　Foula 2026：AI 在減重代謝手術的系統性回顧
- Foula MS, et al. The Evolution of Bariatric and Metabolic Surgery in the Artificial Intelligence Era. *Obes Surg.* 2026;36(10):5478-5497. doi:10.1007/s11695-026-08908-7
- **PMID 42622983**｜系統性回顧，88 篇（術前、術中、術後、LLM）
- 結論（摘要）：AI 在減重手術仍是輔助工具，不是決策工具；LLM 只宜謹慎用於初步衛教
- 原稿 AUC 0.68／0.88 不在摘要，**未核到原文**
- 核對：**摘要**

### A10　Kermansaravi 2025：AI 在減重代謝手術的國際專家共識
- Kermansaravi M, et al. International expert consensus on the current status and future prospects of artificial intelligence in metabolic and bariatric surgery. *Sci Rep.* 2025;15(1):9312. doi:10.1038/s41598-025-94335-0
- **PMID 40102585**｜修正式 Delphi，68 位外科醫師、35 國，28 條陳述全部達 ≥70% 共識
- 內容（摘要）：同意 AI 可協助手術技術評估、轉介與病人／術式選擇；擔心過度依賴 AI 建議；主張訂定倫理規範、把 AI 參與決策寫進知情同意
- 原稿「76% 同意可預測併發症」**未核到原文**
- 核對：**摘要**

### 數位介入（非 AI）有 12 個月資料的 RCT 與統合分析

| 卡號 | 研究 | PMID | 設計／族群 | 數字（摘要） | 備註 |
|------|------|------|-----------|-------------|------|
| D1 | Hesseldal 2022, *J Med Internet Res* 24:e39741, doi:10.2196/39741 | **36149735** | 丹麥 50 個市鎮，n=340（200:140），1 小時面談＋數位教練 | 12 個月 −4.5 kg vs −1.5 kg（P<.001）；HbA1c 組間無差異 | 完成 12 個月者 200 人（127＋73），流失多 |
| D2 | Kohl 2023, *J Med Internet Res* 25:e43426, doi:10.2196/43426 | **37368484** | 德國，n=153，12 週互動式網站（能量密度回饋）vs 非互動網站 | 12 個月追蹤：−4.18 kg（4.7%）vs −1.29 kg（1.5%） | 族群多為代謝健康者，心血管代謝指標無差異 |
| D3 | Gemesi 2024, *Int J Obes* 48:118-126, doi:10.1038/s41366-023-01415-0 | **38017117** | 慕尼黑單中心，n=168，app 多元件介入 12 週 vs 等待 12 週 | 12 週完成者：−3.2 kg（3.2%）vs −0.4 kg；24 週維持 | **沒有 12 個月資料**；原稿 7.8% 不在本篇 |
| D4 | Bertoli 2025（DEMETRA）, *J Med Internet Res* 27:e72054, doi:10.2196/72054 | **41118643** | 義大利 2 中心，n=246，數位療法 app vs 安慰劑 app | **6 個月**：−3.2 kg vs −4.0 kg（中位數），組間無差異；使用量前 25% 者 −7.02 vs −3.50 kg | 高使用者是事後次群組 |
| D5 | Metzendorf 2024, *Cochrane* CD013591.pub2, doi:10.1002/14651858.CD013591.pub2 | **38375882** | 18 篇 RCT，2,703 人 | app vs 無或極少介入，12 個月體重 MD −2.5 kg（95% CI −6.8 至 1.7；3 篇、1,044 人；低確定性） | 結論：未顯示明確效益 |
| D6 | Chew 2022, *J Med Internet Res* 24:e40141, doi:10.2196/40141 | **36129739** | SR／MA，app 減重 RCT | 3 個月減 2.18 kg（高峰），12 個月 1.63 kg；作者稱效果 minimal | |
| D7 | Lee 2026, *J Med Internet Res* 28:e81070, doi:10.2196/81070 | **42081742** | SR／MA，19 篇 RCT，3,556 人，純數位、無一對一真人支持 | SMD 0.26（95% CI 0.14–0.38），95% 預測區間 −0.16 至 0.68（跨 0）；中等確定性；等待名單對照效果最大 | |
| D8 | Nunns 2025, *J Med Internet Res* 27:e65443, doi:10.2196/65443 | **40403296** | 成分網絡統合分析，68 篇試驗、151 個組別 | 衛教資訊＋專家接觸＋獎勵三者組合：6 個月 −2.52 kg（−4.15 至 −0.88），12 個月 −2.11 kg（−4.25 至 0.01） | 探索性模型；**沒有任何試驗組真的用這個組合**；12 個月 CI 碰到 0 |

---

## 三、可以放上投影片的結論（皆已核到摘要以上）

1. **AI 本身的療效還沒被分離出來。**數位或混合照護計畫有效，但沒有單獨評估 AI 元件（A1）。
2. **唯一完成的 12 個月全 AI 生活型態 RCT 結論是「不劣於真人教練」。**AI-DPP 達成複合終點 31.7% vs 31.9%，開始參加率 93.4% vs 82.7%（A2）。
3. **純數位工具 12 個月約減 1.5–4.5 kg。**多數病人達不到 5% 門檻（D1、D2、D5、D6）。
4. **AI 處方系統仍無外部驗證與前瞻性實施證據**（A1）；減重手術 ML 模型 pooled AUC 0.846，但多數高偏誤風險（A8）。

## 四、預計用在哪一頁（2026-11-26 已依使用者「照分配做」寫入：P6.1、P8.1、P9、P13–P16、P22、P50）

- A1、A2、D5–D8 → 中期「穿戴裝置與數位行為介入」兩頁（目前 P7／P8 一帶）或 P9「指引的證據等級」頁，補 2025–2026 新證據
- A2 → 可單獨一頁：AI-DPP 不劣性 RCT（目前簡報尚未引用這篇）
- A8–A10 → 若要補減重手術 AI，接在「AI 研究從預測風險走到輔助決策」頁

## 五、還沒做的事

- AI-DPP 全文（完成率、學歷、各組平均體重變化）：需從 JAMA 網站取得
- Liu 2026 全文（PMC13581758）：原稿多數結論出自這篇，上投影片前建議讀全文確認細節
- Forman RL 試驗正式結果：PubMed 2026-11-26 檢索未見結果論文（P15 寫「進行中」）

---

## 六、OpenEvidence 第 1 題：LLM／agentic AI 在肥胖照護的證據（2026-11-27）

- 來源：使用者在 OpenEvidence 自行查詢後貼回（題目：peer-reviewed evidence for LLM-based or agentic AI systems in obesity care, 2024–2026）
- OpenEvidence 的總結：沒有已完成的 LLM 教練 RCT 證明減重成效；自主執行任務或照護導航的 agent 沒有病人結果資料
- 核對：6 篇新文獻逐篇以 PubMed 摘要核對；Liu 2026（A1）、BETTER4All（A4）已在前面

### B1　Lyra：LLM 聊天機器人 CBT 生活型態計畫（可行性研究）
- Forman EM, et al. Feasibility study of an artificial intelligence chatbot-powered cognitive-behavioral lifestyle modification program. *Ann Behav Med.* 2026;60(1):kaag038. doi:10.1093/abm/kaag038
- **PMID 42847389**（PMC13355595）｜單組可行性研究，8 週，n=17，過重／肥胖（平均 BMI 31.5）
- 數字（摘要）：成本每人每週 1.78 美元；編碼員評 2,288 則訊息、475 次對話**全部判定安全**，專業度平均 8.5/10；
  參與者認為有幫助 69%、有同理心 88%、容易使用 94%；88% 重視 24 小時可用，75% 對 Lyra 產生連結感
- 限制：**未報告減重成效**，作者明言需嚴謹檢驗效果
- 核對：**摘要**，與 OpenEvidence 敘述一致

### B2　Zhao 2026：心血管代謝照護的 LLM 對話代理（範疇回顧）
- Zhao Y, et al. Behavior Change Content and Implementation of Large Language Model-Driven Conversational Agents in Cardiometabolic Care: Scoping Review. *J Med Internet Res.* 2026;28:e89190. doi:10.2196/89190
- **PMID 42456008**（PMC13372078）｜38 篇（19 篇實證、19 篇技術或模擬），2020-01 至 2025-11
- 數字（摘要）：多數定位為第 2 型糖尿病、肥胖的衛教或教練；GPT 家族模型＋RAG 或規則元件的混合架構為主；
  LLM 主要用於客製化說明與情緒回應，自我監測、提醒與安全功能多仍是規則式；
  **完整報告 prompt 只有 34%（13/38），完整報告安全機制 42%（16/38）**；行為或生理結果少，多為先導、短期或單一個案
- 核對：**摘要**，與 OpenEvidence 敘述一致

### B3　Noh 2023：體重管理對話代理（系統性回顧，LLM 普及前）
- Noh E, et al. Conversational Agents for Body Weight Management: Systematic Review. *J Med Internet Res.* 2023;25:e42238. doi:10.2196/42238
- **PMID 37234029**（PMC10257112）｜8 篇（3 篇 RCT、5 篇前後比較），檢索至 2022-12
- 數字（摘要）：只有 3/8 報告明顯減重，**12–15 週減 1.3–2.4 kg**；整體品質低
- 註：「pre-LLM」是 OpenEvidence 依檢索時間的說法，摘要未這樣寫
- 核對：**摘要**

### B4　Motevalli 2026：ChatGPT 用於肥胖管理（Lancet Digital Health 回顧）
- Motevalli M, Boaventura B, Stanford FC. ChatGPT for obesity management: a review of evidence, potential challenges, and clinical implications. *Lancet Digit Health.* 2026;8(5):100980. doi:10.1016/j.landig.2026.100980
- **PMID 41966942**｜主題綜整，37 篇（29 原著、8 回顧），2022-12 至 2025-10
- 數字（摘要）：與專家或指引標準比較，生活型態與營養 **9/12（75%）** 高正確率、減重手術 **5/10（50%）**；
  與其他 AI 工具比較，ChatGPT 整體正確率較高，但與專用工具的比較很少；**高信心等級只有 10/37（27%）**；
  實施障礙六類：正確性、演算法偏誤、文化敏感度、透明與問責、過度依賴、倫理法律
- 核對：**摘要**（較適合第 2 題／P22）

### B5　Suenghataiphorn 2026：LLM 在肥胖領域（系統性回顧）
- Suenghataiphorn T, et al. Large language models in obesity: a systematic review. *Int J Obes (Lond).* 2026;50(3):479-491. doi:10.1038/s41366-025-01992-2
- **PMID 41413746**｜33 篇，檢索至 2025-08，ROBINS-I
- 摘要結論：正確率差異大；有建議不一致、錯誤、複雜情境處理困難、偏誤輸出等限制；需要醫師監督與驗證
- **未核到原文**：OpenEvidence 列出的個別研究數字（ChatGPT-3.5 對 ADA/AACE 20 題、Gemini／GPT-4 81 題與 FDA 資訊相當、
  GPT-4 與 30 位外科醫師共識一致 30%、ASMBS 200 題 83.0%／76.0%／65.0%）**都不在摘要內**，要用需另查原始研究
- 核對：**摘要**（只核到篇數與結論）

### B6　Annor 2025：Gemini 與 Copilot 回答肥胖藥物與手術問題
- Annor E, et al. Assessing online chat-based artificial intelligence models for weight loss recommendation appropriateness and bias in the presence of guideline incongruence. *Int J Obes (Lond).* 2025;49(5):896-901. doi:10.1038/s41366-025-01717-5
- **PMID 39871015**｜橫斷面，10 題（藥物與手術），對照 ADA、AACE 建議
- 數字（摘要）：Copilot 10/10 適當、10/10 完整，2 題偏向特定指引；Gemini 8/10 適當（**另 2 題拒答、要求就醫**，無不適當回答）、5/10 完整，無偏向
- 核對：**摘要**（OpenEvidence 寫「Gemini 8/10」未說明另 2 題是拒答）

### 這一題可以上投影片的結論

1. **LLM 減重教練目前只有可行性資料**：Lyra 17 人 8 週，訊息全數判定安全、成本每人每週 1.78 美元，未報告減重成效（B1）。
2. **LLM 對話代理的研究多為先導或短期**，完整報告 prompt 34%、安全機制 42%（B2）。
3. **LLM 之前的聊天機器人**：8 篇只有 3 篇明顯減重，12–15 週減 1.3–2.4 kg（B3）。
4. 自主執行任務或照護導航的 agent，在這次檢索範圍內沒有病人結果資料（OpenEvidence 總結；我們未另行系統性檢索）。

---

## 七、OpenEvidence 追問：LLM 教練的風險（2026-11-27）

- 來源：使用者在 OpenEvidence 追問後貼回（LLM coaching 的風險與緩解）
- OpenEvidence 的總結：肥胖教練情境沒有前瞻性研究量化傷害率；證據多來自橫斷面回答稽核與心理健康聊天機器人文獻
- 核對：7 篇新文獻以 PubMed 摘要核對；Suenghataiphorn 2026 見 B5

### C1　Ponzo 2024：10 種通用聊天機器人給肥胖病人營養建議
- Ponzo V, et al. Comparison of the Accuracy, Completeness, Reproducibility, and Consistency of Different AI Chatbots in Providing Nutritional Advice: An Exploratory Study. *J Clin Med.* 2024;13(24):7810. doi:10.3390/jcm13247810
- **PMID 39768733**（PMC11677083）｜探索性研究；2 個案例連續 3 天問 10 種聊天機器人，3 位營養師評分
- 數字（摘要）：
  - 案例 1（35 歲男性，肥胖無共病）：正確率最高 ChatGPT 3.5 **67.2%**、最低 Copilot **21.1%**；重現性最低 ChatGPT 4.0 **50%**、ChatGPT 3.5 52.8%（最高 Chatsonic 86.1%）
  - 案例 2（65 歲女性，肥胖＋第 2 型糖尿病＋肌少症＋慢性腎病）：**沒有一個聊天機器人正確率達 50%**
  - 多數聊天機器人在同一回答中**同時建議減少與增加蛋白質攝取**
- 核對：**摘要**，與 OpenEvidence 敘述一致

### C2　Bragazzi 2025：LLM 與營養系學生的營養知識比較
- Bragazzi NL, et al. Comparative analysis of AI on human nutrition knowledge. *PLoS One.* 2025;20(12):e0336577. doi:10.1371/journal.pone.0336577
- **PMID 41359659**（PMC12685196）｜GNKQ-R 問卷，4 種 LLM 對照人類
- 數字（摘要）：LLM 平均 77.3/88，與營養系學生相當；ChatGPT-4 **82/88**，高於營養系學生 79.3、英文系學生 67.7；
  作者提醒 LLM 難以依臨床複雜度與個體差異給個人化建議
- 核對：**摘要**

### C3　Asgari 2025：LLM 產生臨床紀錄的幻覺率
- Asgari E, et al. A framework to assess clinical safety and hallucination rates of LLMs for medical text summarisation. *NPJ Digit Med.* 2025;8(1):274. doi:10.1038/s41746-025-01670-7
- **PMID 40360677**（PMC12075489）｜18 種實驗設定，12,999 句經臨床人員標註
- 數字（摘要）：**幻覺率 1.47%、遺漏率 3.45%**；調整 prompt 與流程後，重大錯誤降到低於文獻中的人工記錄錯誤率
- **圖 2 核對（使用者 2026-11-27 提供截圖，數值為讀長條圖，約略值）**：
  - 幻覺句共 **191 句**；各 prompt 幻覺率約 0.1%–5.3%（整體 1.47%）
  - 依類型（重大／全部）：捏造 ≈48/82、否定 ≈23/56、脈絡 ≈4/33、因果 ≈10/20 → 重大合計約 85/191（**約 44%**，OpenEvidence「近一半」大致成立）
  - 依段落：**Plan 段最多，約 76 句（重大約 42）**，其次 Assessment 約 41；OpenEvidence「Plan 段最容易出錯」成立
  - 上投影片時寫「約 4 成為重大錯誤」「計畫段最多」，並註明讀圖；圖要自繪，不直接貼原圖
- 註：這篇是病歷記錄生成；作者單位為 Tortus AI（廠商）。**P20 的病歷貼稿是樣板拼接、非 AI 生成**，所以這篇可用來說明「為什麼貼稿不用 LLM 生成」，不能說成本院工具的錯誤率
- 核對：**摘要**

### C4　Diel 2026：LLM 聊天機器人的心理健康傷害（範疇回顧）
- Diel A, et al. A scoping review on the mental health harms of LLM-based chatbots. *NPJ Digit Med.* 2026;9(1):644. doi:10.1038/s41746-026-03054-x
- **PMID 42624944**（PMC13493897）｜119 篇
- 內容（摘要）：概念性文獻提到的傷害包括幻覺、諂媚（sycophancy）、偏誤、資料安全；情境題研究顯示回答心理健康問題不符臨床標準；過度依賴與情緒依附和心理症狀相關
- 未核到原文：「幻覺是最常被提到的傷害」摘要沒有排序
- 核對：**摘要**

### C5　Hua 2025：心理健康聊天機器人從規則式到 LLM（系統性回顧）
- Hua Y, et al. Charting the evolution of artificial intelligence mental health chatbots from rule-based systems to large language models: a systematic review. *World Psychiatry.* 2025;24(3):383-394. doi:10.1002/wps.21352
- **PMID 40948070**（PMC12434366）｜160 篇（2020–2024）
- 數字（摘要）：2024 年新研究中 LLM 型佔 **45%**；但 LLM 研究只有 **16% 做到臨床療效測試**，77% 仍在早期驗證；
  行銷宣稱「AI-powered」與實際架構不符，很多只是規則式腳本
- 核對：**摘要**（OpenEvidence 只引用它談隱私與偏誤，摘要的 16% 數字更有用）

### C6　Kleinman 2026：LLM 用於治療的前景與風險（社論）
- Kleinman RA, Torous J, Danilewitz M. Use of Large-Language Models for Therapy: Promise and Perils. *Ann Intern Med.* 2026;179(4):600-601. doi:10.7326/ANNALS-25-04914
- **PMID 41698202**｜Editorial，**PubMed 無摘要**
- **未核到原文**：諂媚、長對話安全防護失效、模型靜默更新需重測、互動誘因、建議先篩檢飲食障礙等說法，全部無法從摘要核對

### C7　Clusmann 2026：醫療 LLM 的安全與資安（Nature 回顧）
- Clusmann J, et al. Safety and security of large language models in healthcare. *Nature.* 2026;656(8128):577-589. doi:10.1038/s41586-026-10687-1
- **PMID 42618758**｜Review
- 內容（摘要）：把資安危害對應到臨床 AI 開發階段（設計、資料、模型、推論、環境），整理安全層級並依臨床相關性分類威脅
- 未核到原文：長對話效能下降、代理過度授權、「提醒與安全升級維持規則式」等具體說法不在摘要
- 註：適合第Ⅲ段資安頁（P45「AI 本身成為新破口」）當學術出處
- 核對：**摘要**

### 這一段可以上投影片的結論

1. **病人越複雜，通用聊天機器人越不可靠**：肥胖合併糖尿病、肌少症、慢性腎病的案例，10 種都未達 50% 正確率；同一問題隔天再問，重現性最低 50%（C1）。
2. **知識題答得好，個人化建議答不好**：ChatGPT-4 營養知識 82/88，高於營養系學生，但作者提醒個人化建議受限（C2、C1）。
3. **LLM 產生臨床紀錄的幻覺率 1.47%、遺漏率 3.45%**；幻覺句約 4 成屬重大錯誤，最常出現在治療計畫段（C3，圖 2 讀圖）。
4. **心理健康領域的 LLM 聊天機器人只有 16% 做到臨床療效測試**（C5）。

---

## 八、OpenEvidence 追問：醫師審核 AI 輸出的工作量（2026-11-27）

- 來源：使用者在 OpenEvidence 追問後貼回（監督 AI 輸出會增加多少醫師工作）
- OpenEvidence 的總結：證據來自 AI 草擬病人訊息與病歷書寫工具，不是肥胖教練；負擔感與倦怠改善，但每則訊息花的時間常沒有減少
- 核對：PubMed 摘要；OpenEvidence 引用的 Harris 2024 是 JAMA 新聞稿，**改引原始研究 Garcia 2024**

### E1　Garcia 2024：AI 草擬病人訊息回覆（Stanford，5 週）
- Garcia P, et al. Artificial Intelligence-Generated Draft Replies to Patient Inbox Messages. *JAMA Netw Open.* 2024;7(3):e243201. doi:10.1001/jamanetworkopen.2024.3201
- **PMID 38506805**（PMC10955355）｜前瞻性單組品質改善研究，基層醫療與腸胃肝膽科，162 位臨床人員（問卷完成 73 人，45.1%）
- 數字（摘要）：AI 草稿使用率平均 **20%**；**閱讀、撰寫、回覆時間都沒有改變**；任務負荷分數 61.31→47.26（P<.001）、工作耗竭分數 1.95→1.62（P<.001）
- OpenEvidence 原引：Harris E. *JAMA.* 2024;331(17):1440（**PMID 38607634，新聞稿**），投影片引原始研究
- 核對：**摘要**

### E2　Jeanselme 2026：Epic AI 草稿工具與回覆時間、下班後回覆（Columbia）
- Jeanselme V, et al. AI-Generated Draft Response Tool, Message Turnaround Time, and After-Hours Replies Among Health Care Professionals. *JAMA Netw Open.* 2026;9(10):e2641364. doi:10.1001/jamanetworkopen.2026.41364
- **PMID 42961417**（PMC13723026）｜回溯世代，983,154 則回覆、1,542 位臨床人員，2023-03 至 2025-05
- 數字（摘要）：
  - **導入工具後整體回覆時間反而增加 8.6%**（95% CI 4.6–12.9%）
  - 實際使用草稿的回覆，回覆時間減少 29.5%（95% CI −34.5% 至 −24.1%）
  - 整體下班後回覆負擔沒有減少（+0.61 個百分點，P=.46）；下班時間收到的訊息，使用工具後下班回覆**增加** 4.52 個百分點；上班時間收到的檢驗結果問題，下班回覆減少 3.67 個百分點
  - 下班相關結果對「上班時間」定義敏感
- **未核到原文**：OpenEvidence 的「上班時間收到減少約 35–43%、下班收到減少約 13–24%」不在摘要；而且 OpenEvidence **沒提到導入後整體回覆時間增加 8.6%**
- 核對：**摘要**

### E3　Poursoltan 2026：醫師修改 AI 草稿的內容與耗時（UC San Diego）
- Poursoltan L, et al. Physician Edits to AI-Drafted Patient Messages and Their Impact on Clinical Workload. *NEJM AI.* 2026;3(9):AIoa2501034. doi:10.1056/AIoa2501034
- **PMID 42932708**｜品質改善研究，14,350 則 AI 輔助回覆、1,131 位醫師，2024-04 至 2025-08
- 數字（摘要）：所有 15 類修改都使回覆時間變長；增幅最大的是判讀影像（**+70.1%**）、釐清或排除診斷（+63.9%）、判讀檢驗（+60.8%）；
  **最常見的修改是安排門診與生活型態建議**；累積負擔最大的是排程、**生活型態建議**、轉介協調
- **未核到原文**：OpenEvidence 的「用藥管理 40–50%、生活型態 20–40%、行政與同理心 <20%」分級來自圖 3，摘要沒有
- 核對：**摘要**

### E4　Zhao 2025：AI 工具與臨床文書負擔（統合分析）
- Zhao J, et al. Application of artificial intelligence tools and clinical documentation burden: a systematic review and meta-analysis. *BMC Med Inform Decis Mak.* 2025;26(1):29. doi:10.1186/s12911-025-03324-w
- **PMID 41444884**（PMC12836966）｜23 篇（12 篇非隨機有同期對照、11 篇前後比較），方法品質普遍低、異質性大
- 數字（摘要）：14 篇合併，文書負擔與倦怠 **SMD −0.71**（95% CI −0.93 至 −0.49）；醫師有審閱修改 AI 草稿的研究，文書時間 **SMD −0.72**（−0.99 至 −0.45）；AI 產生的紀錄品質至少與人工相當
- 核對：**摘要**（**沒有 RCT**）

### E5　Brodeur 2026：AMIE 對話式診斷 AI 在基層急症門診（Lancet）
- Brodeur PG, et al. Conversational diagnostic artificial intelligence in ambulatory primary care: a prospective feasibility study. *Lancet.* 2026;408(10565):1732-1744. doi:10.1016/S0140-6736(26)01535-7
- **PMID 42849491**｜前瞻性單中心單組可行性研究（NCT06911398），收 114 人、98 人完成；Alphabet 資助
- 數字（摘要）：病人在門診前與 AMIE 對話，醫師安全監督者全程監看：**安全暫停 0 次**，監督者記錄 **1 次幻覺**、5 次補充臨床資訊；
  臨床評估者對 17 項標準的好評 87–100%；看過逐字稿的醫師 33/44 認為有助看診準備
- **未核到原文**：「作者呼籲試驗量測醫師工作量與所需監督量」不在摘要
- 核對：**摘要**

### 未核到原文
- Sharko M, Cole CL. *JAMA Netw Open.* 2025;8(3):e250462（PMID 40067306）：PubMed 無摘要，「告知 AI 撰寫後病人滿意度下降」無法核對
- Mastrianni A, et al. *npj Digital Medicine* 2026（doi:10.1038/s41746-026-03185-1）：PubMed 查無收錄

### 這一段可以上投影片的結論

1. **AI 草稿減輕負擔感，但不一定省時間**：Stanford 162 人 5 週，負荷與耗竭分數下降，閱讀與回覆時間不變（E1）。
2. **導入 AI 草稿後整體回覆時間增加 8.6%**；下班時間收到的訊息，使用工具後下班回覆反而增加（E2，98 萬則回覆）。
3. **醫師最常修改的是生活型態建議與排程**；判讀影像、檢驗與診斷的修改最耗時（+60–70%）（E3）。
4. **AI 文書工具的統合分析：負擔與文書時間中度下降（SMD 約 −0.7），但沒有 RCT、品質普遍低**（E4）。


## 九、OpenEvidence 追問：數位／AI 生活型態支持＋GLP-1 RA，是否比單用藥更好（2026-11-27）

> 使用者自行查詢 OpenEvidence 後貼回。8 筆引用中 7 筆查 PubMed 核到（摘要以上），1 筆為 ADA 2026 會議摘要，PubMed 未收錄。
> OpenEvidence 的總結成立：**沒有任何 RCT 比較「數位／AI 支持＋GLP-1 RA」與「單用 GLP-1 RA」**；現有資料全是觀察性，且研究的都是一般數位工具，**不是 AI**。

| 代號 | 文獻 | PMID | 核對層級 | 核到的內容 | OE 說法核對 |
|---|---|---|---|---|---|
| F1 | Davey B. J Med Internet Res 2026;28:e100728（澳洲 Mosh 直營平台，回溯） | 42976342 | 摘要 | n=6113；app＋藥 vs 只用藥：≥5% 減重 aOR 1.38–2.22（60／120／180 天）、≥10% aOR 1.67–1.97（120／180 天）、≥15% aOR 1.99（180 天）；只有「進度記錄」與減重速度相關（β=0.26 個百分點／30 天）；作者明寫非因果，整體軌跡差異小 | ✅ 正確。**這篇有「只用藥」對照組**（自選，非隨機） |
| F2 | Johnson H. J Med Internet Res 2025;27:e69466（英國 Voy 平台服務評估） | 40164173 | 摘要 | n=57,975；投入 54.2% vs 未投入；第 3 月 9% vs 5.9%、第 5 月 11.53% vs 8%；投入以教練出席、app 使用、量體重定義 | ✅ 數字正確。⚠️ OE 沒提：**前三位作者是 Voy 公司（Menwell Ltd）員工**；比較的是投入 vs 未投入，無只用藥組 |
| F3 | Ali SH. Int J Obes 2026;50(6):1276-82（新加坡 NOVI，單組） | 41957114 | 摘要 | n=708，86% 口服 semaglutide 14 mg；12 月減重 12.7%、18 月 14.7%；app 投入高者多減 2.0–2.2%；東亞裔與高血糖者減得較少 | ✅ 方向正確；OE 寫「接近試驗結果」為其詮釋，摘要未如此比較。作者含 NOVI Health 人員 |
| F4 | Heisey HD. Diabetes Obes Metab 2026;28(8):6533-49（敘述性回顧） | 42244474 | 全文 | 全文原句：肥胖藥物的服藥遵從介入「remain underexplored」；T2DM 的 RCT 顯示科技介入對遵從有「modest but meaningful」改善；GLP-1 RA 的數位工具「primarily supporting trial engagement rather than real-world adherence」 | ✅ 三句皆核到全文 |
| F5 | Cook G. J Med Internet Res 2026;28:e104227（觀點文章） | 42709474 | 摘要 | 提出「藥物開啟的習慣養成窗口」假說，將證據分 established／observational／hypothesized；呼籲做含停藥後追蹤的 RCT | ✅ 正確。屬觀點，不是研究 |
| F6 | Chu J. EClinicalMedicine 2025;88:103464（統合分析） | 40926900 | 摘要 | 33 篇 RCT、12,028 人；MD −7.13 kg；體重證據確定性中到低 | ⚠️ **OE 敘述易誤讀**：對照組是「生活型態＋安慰劑」，所以 −7.13 kg 是**藥物在生活型態之上的效果**，不是生活型態加在藥物之上的效果；屬藥物試驗數字，**依使用者指示不放 12/13 場** |
| F7 | Lundgren JR. N Engl J Med 2021;384:1719-30（S-LiTE RCT） | 33951361 | 書目 | 運動＋liraglutide 維持減重優於單一方式 | ✅ 書目核到；為督導運動，不是數位介入；藥物試驗，本場不用 |
| F8 | Johnson H, Reisel D, Huang D. ADA 2026 摘要 1661-P（T2D，n=7,642） | — | 未核到原文 | OE：完全投入 −19.5% vs 未投入 −14.6%（12 月） | ❓ PubMed 未收錄、未核到；作者與 F2 同為 Voy 公司，**不建議引用** |

### 可以放上投影片的結論
1. **「藥物＋數位管理」目前沒有隨機對照證據**：沒有試驗比較「數位支持＋GLP-1 RA」與「單用 GLP-1 RA」（F1–F5）。
2. **觀察性研究方向一致，但有自選偏誤**：澳洲 6,113 人，用 app 者達 ≥10% 減重的勝算高 1.7–2.0 倍（F1）；英國 57,975 人，投入者第 5 月 11.5% vs 8.0%，作者為平台公司員工（F2）。
3. **有用的功能是自我記錄**：F1 只有「進度記錄」與減重速度相關；F3 也是記錄頻率越高、結果越好。
4. **服藥持續率**：肥胖藥物的遵從介入研究仍少，數位工具多用在試驗中的參與，不是真實世界的持續用藥（F4，全文）。
5. 以上研究的都是一般 app／教練，**沒有 AI 特有的對照資料**。

## 十、OpenEvidence 追問：東亞／台灣族群的肥胖 ML 模型與跨族群表現（2026-11-27）

> 使用者自行查詢後貼回。8 筆引用全部查到 PubMed；其中 3 筆是社論／評論、無摘要，內文數字未核到。
> OpenEvidence 的總結成立：**查到的研究沒有台灣本土模型**，東亞研究多為中國單一族群、橫斷面、只做內部驗證，無法量化跨族群表現差異。

| 代號 | 文獻 | PMID | 核對層級 | 核到的內容 | OE 說法核對 |
|---|---|---|---|---|---|
| G1 | Lin W. Front Endocrinol 2023;14:1292167（福建寧德，橫斷面 2011–12） | 38047114 | 摘要 | 5,236 名過重成人；CatBoost 測試集 AUC 0.87、五折交叉驗證 0.87±0.022；主要預測因子腰圍、臀圍、女性、收縮壓 | ✅ 數字正確。⚠️ 以腰臀圍預測肥胖，屬 G4 所說的循環預測 |
| G2 | Du J. Sci Rep 2024;14:22424（健檢資料） | 39342032 | 摘要 | 1,678 筆；XGBoost 分三類：BMI <25、25–30、≥30 | ⚠️ OE 稱「class 1／class 2 obesity」，實際 25–30 是過重；以體組成預測 BMI 分類，循環性高 |
| G3 | Zhang Z. Endocrine 2024;86(2):600-11（中國高中生，1 年前瞻） | 38856840 | 摘要 | 1,241 人、1 年後 204 人（16.4%）過重；LightGBM AUC 0.961；過採樣改善表現 | ✅ 方向正確；「既往兒童模型準確率 0.56–0.95」不在摘要，**未核到** |
| G4 | Jamali M. NPJ Digit Med 2026（系統性回顧） | 42432037 | 摘要 | 17 篇（3 篇縱貫、14 篇橫斷面），**只有 1 篇做獨立外部驗證**，校準幾乎未報告；橫斷面 AUC 最高 0.979，但多受循環預測影響；縱貫研究只有 1 篇報 AUC（0.81）；結論：AI 肥胖模型應視為探索性輔助工具 | ✅ 全部核到 |
| G5 | Smit RAJ. Nat Med 2025;31(9):3151-68（多族裔多基因分數） | 40691366 | 摘要 | 510 萬人（東亞 8.4%、歐洲 71.1%）；多族裔 PGS 解釋 BMI 變異：英國生物資料庫歐洲裔 17.6%，其他族群從**東亞裔美國人 16%** 到烏干達鄉村 2.2% | ⚠️ OE 寫「非洲裔約 7%」為圖中 UKBB 數字，摘要最低是 2.2%；OE **沒提東亞裔 16% 與歐洲裔接近**。這是基因分數，不是臨床 ML 模型 |
| G6 | Wee CC. Ann Intern Med 2022;175(11):1606-7（評論） | 36191313 | 書目 | 無摘要 | ❓ 亞裔美國人各次族群肥胖盛行率 13.2%（華裔）–28.7%（菲律賓裔）**未核到**，可能出自同期另一篇原始研究 |
| G7 | Lim S. Nat Rev Endocrinol 2026;22(10):615-24（觀點） | 42045672 | 摘要 | 亞洲人在較低 BMI 即有內臟與異位脂肪、β 細胞儲備低、肌少型肥胖；沿用西方標準會系統性低估；主張以脂肪與器官功能定義臨床肥胖（接軌 Lancet Commission） | ✅ 核到 |
| G8 | Bajaj SS. Ann Intern Med 2024;177(8):1127-9（社論） | 39038288 | 書目 | 無摘要 | ❓ WHO 亞洲切點 23／27.5、印度 25、中國 28 屬已知標準，但**未在此文核到** |

### 可以放上投影片的結論
1. **台灣沒有本土驗證的肥胖 ML 模型**（此次檢索範圍內）；東亞研究以中國單一族群、橫斷面、內部驗證為主（G1–G3）。
2. **17 篇肥胖 ML 研究只有 1 篇做外部驗證**；高 AUC 常來自用身高體重、腰圍預測 BMI 定義的肥胖（G4）。
3. **標籤本身有族群偏誤**：多數模型用 BMI 定義肥胖，亞洲人在較低 BMI 即有代謝風險，用西方 BMI ≥30 訓練的模型可能漏掉亞洲病人（G7；台灣切點 24／27 為國健署標準，非本文獻）。
4. 基因分數跨族群表現落差大，但東亞裔美國人 16% 與歐洲裔 17.6% 接近（G5），不宜寫成「東亞表現差」。

## 十一、OpenEvidence 追問：AI／ML 輔助選擇或調整減重藥物（2026-11-27）

> 使用者自行查詢後貼回。3 篇期刊文獻皆查到 PubMed；第 4 筆是 FDA Orange Book 網頁，未核。
> OpenEvidence 的總結成立：**沒有找到前瞻或外部驗證過的 AI 選藥／調劑量工具，也沒有報告病人結果的試驗**。與 P12 一致：TiP DecScore 是 T2D、回溯、醫師開藥時看不到分數；CTS-GRS 是會議摘要層級 post-hoc。

| 代號 | 文獻 | PMID | 核對層級 | 核到的內容 | OE 說法核對 |
|---|---|---|---|---|---|
| H1 | Kuryłowicz A, Czupryniak L. Diabetes Obes Metab 2026;28(12):10950-60（敘述性回顧） | 42634284 | 摘要 | 非 T2D 肥胖試驗中，無反應（減重 <5%）約 10%，真實世界更高；**目前最可行的預測因子是用藥早期的反應**；GLP1R／GIPR 的 GWAS 關聯為自陳、單一世代、未重複，只能產生假說，不宜據以做個人基因檢測；結論：沒有單一基線特徵能可靠預測反應 | ✅ 方向正確。rs10305420 位點名稱、SURMOUNT-5 20.2% vs 13.7% 不在摘要，**未在此文核到**（SURMOUNT-5 為藥物試驗，本場不用） |
| H2 | Wee CC, Li T, Batch BC, Wong JB. Ann Intern Med 2026;179(8):1203-5（社論） | 42296502 | 書目 | 查到書目，未取得內文 | ❓「69 篇只有 6 篇直接比較、1 篇 semaglutide vs tirzepatide」**未核到**；ACP 有條件建議 semaglutide／tirzepatide 為第一線，見 `refs-glp1-discontinuation-verified.md` G9 |
| H3 | Moiz A. Ann Intern Med 2026;179(10):1412-29（系統性回顧更新） | 42673585 | 摘要 | 38 篇 RCT、25,816 人；扣除安慰劑減重 liraglutide −5.8% 至 tirzepatide −19.0%；腸胃副作用 76.0% vs 40.1% | ✅ 書目正確。OE 引用的 semaglutide 7.2 mg vs 2.4 mg 不在摘要，未核。屬藥物試驗，**本場不用** |
| H4 | FDA Orange Book | — | 未核 | orforglipron 逐步調劑量 | ❓ 網頁，未核 |

### 可以放上投影片的結論
1. **沒有前瞻驗證過的 AI 選藥或調劑量工具**（此次檢索範圍內）；選藥仍依 RCT 與網絡統合分析（H1–H3）。
2. **目前最可行的個人化依據是用藥早期反應**，基因與代謝標記需前瞻重複驗證才能用於臨床（H1）。可接 P12「CTS-GRS 為會議摘要層級」的保留語氣。

## 十二、第九–十一節的用法（2026-11-27 依使用者「照用法做」寫入，不新增頁）

- **P11**：key-box 加 F1 結論（6,113 人、勝算 1.7–2.0 倍、尚無隨機試驗）＋ cite（Davey、Johnson、Heisey）＋新增講稿（F2 廠商作者、F4 服藥持續率）。
- **P6.1**：kb-note 加 G4（17 篇僅 1 篇外部驗證）與「台灣尚無本土驗證模型」；cite 補 Jamali、Lim；講稿補循環預測與 BMI 切點族群偏誤（G7）。
- **P12**：kb-note 加 H1（未查到前瞻驗證的 AI 選藥工具；早期反應為主要依據）＋新增講稿。字型沒有「ł」，畫面寫 Kurylowicz。
- 不用：F6、F7、H3 藥物試驗數字；F8、G6、G8、H2 未核到內文的數字；G5 基因分數（易誤讀為東亞表現差）。
