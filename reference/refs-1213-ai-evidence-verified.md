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

## 四、預計用在哪一頁（待使用者決定）

- A1、A2、D5–D8 → 中期「穿戴裝置與數位行為介入」兩頁（目前 P7／P8 一帶）或 P9「指引的證據等級」頁，補 2025–2026 新證據
- A2 → 可單獨一頁：AI-DPP 不劣性 RCT（目前簡報尚未引用這篇）
- A8–A10 → 若要補減重手術 AI，接在「AI 研究從預測風險走到輔助決策」頁

## 五、還沒做的事

- AI-DPP 全文（完成率、學歷、各組平均體重變化）：需從 JAMA 網站取得
- Liu 2026 全文（PMC13581758）：原稿多數結論出自這篇，上投影片前建議讀全文確認細節
- Forman RL 試驗正式結果是否已發表：未查
