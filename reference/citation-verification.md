# 引用查證報告：AI×肥胖醫學演講素材

**查證對象**：台灣肥胖醫學會 2026 南區學術研討會演講素材（2026-09-20）
**查證日期**：2026-08-14
**查證方法**：WebSearch + WebFetch 追查原始論文／官方新聞稿，逐條交叉比對數字與語境
**查證範圍**：11 條主張（A. GLP-1藥物與AI參與度、B. 副作用/療效AI預測、C. Agentic AI真實世界研究、D. 消費端平台）

---

## 圖例

- ✅ **真實存在**：原始出處找得到，數字與語境吻合
- ⚠️ **部分吻合但有出入**：數字本身查得到出處，但語境、分組、來源被抽換／嫁接／誇大
- ❌ **查無此事，疑似幻覺**：找不到任何對應來源
- 🔍 **證據不足，無法判斷**

---

## A. GLP-1藥物與AI參與度

### 1. Semaglutide：非AI參與組 7.8% vs AI參與組 9.5%

**查證結果：⚠️ 數字真實存在，但語境被嫁接（誤導性引用）**

原始出處：Johnson H, Huang D, Liu V, Al Ammouri M, Jacobs C, El-Osta A. "Impact of Digital Engagement on Weight Loss Outcomes in Obesity Management Among Individuals Using GLP-1 and Dual GLP-1/GIP Receptor Agonist Therapy: Retrospective Cohort Service Evaluation Study." *J Med Internet Res* 2025;27(1):e69466. DOI: 10.2196/69466. (PMC11997532)

論文原文：「At month 5, participants using tirzepatide achieved a mean weight loss of 13.9%... significantly greater than the 9.5%... observed in semaglutide users (P<.001)」——**9.5% 是第5個月「semaglutide 對比 tirzepatide」的藥物間比較，不是「AI參與 vs 非AI參與」的比較**。

這篇論文確實也有「數位參與（engaged）vs 未參與（non-engaged）」的分析，但那是兩種藥物合併計算的結果：第5個月 engaged 11.53% vs non-engaged 7.97%（兩者皆非semaglutide專屬數字）。**「7.8%」這個數字本身在全文中完全查不到**，最接近的是 7.97%（四捨五入應為8.0%而非7.8%）。

**結論**：投影片把「藥物比較」的真實數字（9.5%）錯配成「AI參與比較」，並搭配一個查無出處的「7.8%」。這是典型的「真數字、假語境」混淆。

**信心程度**：中（數字9.5%真實可查，但整條主張的因果框架是誤植的）

---

### 2. Tirzepatide：非AI參與組 11.2% vs AI參與組 13.9%

**查證結果：⚠️ 數字真實存在，但語境被嫁接（誤導性引用）**

同樣出自上述 JMIR 2025;27:e69466 論文——13.9% 是第5個月「tirzepatide 對比 semaglutide」的**藥物間**比較數字，不是AI參與度的比較。

另外還存在一篇**真正**針對 tirzepatide 數位參與度的研究：Johnson H, Clift AK, Reisel D, Huang D. "Digital Engagement Significantly Enhances Weight Loss Outcomes in Adults With Obesity Treated With Tirzepatide: Retrospective Cohort Study of a Digital Weight Loss Service." *J Med Internet Res* 2026;28:e83718. DOI: 10.2196/83718. (PMC12856402)

此研究提供真正的 engaged vs non-engaged 數字（按月）：
| 月數 | Engaged | Non-engaged |
|---|---|---|
| 第2月 | -7.39% | -6.44% |
| 第6月 | -16.48% | -13.39% |
| 第12月 | -22.89% | -17.55% |

**沒有任何時間點出現 13.9% vs 11.2% 這組配對**。「11.2%」查無出處。

**結論**：與主張1同樣的問題——真數字被抽離原始語境（藥物比較）錯貼到AI參與度敘事上，且確實存在的tirzepatide參與度研究反而完全沒被引用。

**信心程度**：中（13.9%真實可查但語境錯誤；11.2%查無此數）

---

### 3. GLP-1全球市場規模：2024年385億美元 → 2030年1300億美元（成長3.4倍），標注來源 Grand View Research、PwC、J.P. Morgan

**查證結果：⚠️ 兩個數字各自有出處，但不是同一份報告的數字，且標注來源與實際發布機構不符**

- **$38.5B（2024）**：查到出處是 **DelveInsight** 的市場報告，且範圍限定在「美國、EU4、英國、日本」等主要市場，**不是全球市場**，也**不是 Grand View Research**。
- **Grand View Research 自家實際數字**：GLP-1受體促效劑（廣義）市場預估 2024年約 $53.46B → 2030年 $156.71B；若限定「GLP-1減重藥物」細分市場則是 2024年 $13.8B → 2030年 $48.8B。**這兩組數字都跟投影片的 $38.5B/$130B 對不上**。
- **$130B（2030）**：可追溯到高盛（Goldman Sachs）2023年的原始估計，以及UBS 2026年調降後的估計（原本超過$150B下修到$130B），**都不是PwC或J.P. Morgan發布的數字**。
- **J.P. Morgan 官網（jpmorgan.com/insights）實際公開的預測反而是「incretin市場2030年將達 $200B」**，與投影片標注「J.P. Morgan」支持 $130B 直接矛盾。
- PwC 官網頁面（GLP-1 trends and business models）因反爬蟲機制無法直接讀取原文核對具體數字。

**結論**：投影片呈現的「385億→1300億、成長3.4倍」在算術上自洽（38.5×3.4≈130.9），但這組配對的三個標注來源（GVR/PwC/JPM）沒有一個真的發布過這兩個數字的組合；反而J.P. Morgan公開數字（$200B）與投影片暗示的立場相反。這是「查得到片段真實數字、但來源標籤是拼裝/誤植」的典型案例。

**信心程度**：低（數字片段可查但來源標注不實）

---

## B. GLP-1副作用與療效AI預測

### 4. Mayo Clinic 與 Phenomix Sciences 2025年研究：GRS預測GLP-1腸胃道副作用，高分組噁心68% vs 低分組30%

**查證結果：✅ 真實存在，但需標注重要限定條件**

真實研究，於 2025年5月 Digestive Disease Week (DDW 2025) 發表，研究團隊：Andres Acosta MD PhD（Mayo Clinic / Phenomix共同創辦人）、Thomas Fredrick MD（發表人）等，與 Phenomix Sciences 合作。研究標題：「A Genetic Risk Score Associated with Nausea Resulting from GLP-1 Agonist Treatment: A Post-Hoc Analysis of a Randomized Controlled Trial of Liraglutide」。

原文確認：「Patients with a high GRS were more than twice as likely to experience nausea from liraglutide... compared to those with a low score (68% vs. 30%).」

**重要限定條件（投影片未說明，同行可能會追問）**：
1. **這是針對 liraglutide 的post-hoc分析，不是semaglutide或tirzepatide**——若投影片籠統寫「GLP-1」而未註明藥物，容易讓聽眾誤以為適用於目前臨床最常用的semaglutide/tirzepatide。
2. **樣本數僅 110人**（既有RCT的次分析），樣本量偏小。
3. 目前查到的是**DDW 2025會議摘要/新聞稿層級**的發表，尚未確認是否已有同行審查期刊全文發表（PR Newswire / Patient Care Online / HIT Consultant 等二手報導可查，但未查到期刊全文）。

**信心程度**：高（核心數字68% vs 30%真實可查），但務必標註「liraglutide、n=110、會議摘要層級」等限定條件

**來源**：PR Newswire (2025-05-07) "Mayo Clinic Study Uses Phenomix AI Algorithm to Predict GLP-1 Side Effects"；Patient Care Online "Genetic Risk Score Identifies Individuals Likely to Report Adverse Events from GLP-1 Mimetic Therapy"

---

### 5. 副作用預測列線圖(nomogram) AUC值0.84-0.86

**查證結果：⚠️ AUC數值範圍真實存在，但出自完全不同、不相關的另一篇研究**

查到吻合的AUC數字：Gao R, Li Y, Li A, Zhou P, Zong H, Li Y. "Risk factor screening and prediction modeling of gastrointestinal adverse reactions caused by GLP-1RAs." *Frontiers in Endocrinology*, 2024-12-05. DOI: 10.3389/fendo.2024.1502050. 該研究之列線圖模型 AUC 為訓練集0.855、驗證集0.836。

**但這篇研究與主張4（Mayo Clinic/Phenomix的遺傳風險評分研究）完全無關**：這篇用的是傳統臨床風險因子（年齡、性別、腸胃病史、合併用藥數量），研究對象是第2型糖尿病患者使用GLP-1RA，**不涉及基因檢測或AI遺傳風險評分**。Mayo Clinic/Phenomix的新聞稿中並未提及任何AUC或列線圖數值。

**結論**：如果投影片把這個AUC值當成「Mayo Clinic/Phenomix的GRS模型表現」在引用，這是**兩篇不相關研究被混為一談**的典型錯誤。若只是單獨引用「有研究做過GLP-1副作用預測列線圖，AUC約0.84-0.86」，則這句話本身是真的，但需要換成正確的出處（Gao et al. 2024，非Mayo/Phenomix）。

**信心程度**：中（AUC數字真實，但很可能被錯誤歸因到另一項研究）

---

### 6. PrecisionLife 與 Ovation 2026年研究：2500+遺傳特徵/1100個基因，分類準確率95%、PPV 96%

**查證結果：⚠️ 部分吻合——特徵與基因數量真實，但「95%準確率/96% PPV」查無出處**

真實新聞稿：PrecisionLife Ltd. 與 Ovation.io 合作，2026年2月25日發布Phase 1研究結果（PR Newswire）。確認內容：
- Phase 1 使用 **4,600名患者**資料
- 識別出 **超過2,500個遺傳特徵（genetic signatures）**，對應到 **1,100個基因**
- 涉及 **15個主要生物機制**
- 100%的患者都能被生物標記覆蓋，可分為「強反應者」與「弱反應者」

**但「分類準確率95%」「PPV 96%」這兩個具體數字，在PR Newswire新聞稿全文與precisionlife.com/glp1官網頁面中都查不到**，官方說法只有質性描述（識別強弱反應者），沒有給出量化的準確率/PPV指標。

**結論**：這條主張的「骨架」（2500特徵、1100基因、Phase 1）是真的，但「95%/96%」這兩個關鍵效能數字疑似是AI摘要工具自行生成、查無實據。

**信心程度**：中（特徵/基因數字真實，準確率數字疑似幻覺）

**來源**：PR Newswire (2026-02-25) "PrecisionLife and Ovation identify first potential genetic biomarkers to quantitatively predict GLP-1 efficacy response"；precisionlife.com/glp1

---

### 7. 「TiP DecScore」臨床決策支援系統：使用AI建議後糖尿病患者HbA1c控制率從46%提升到64%

**查證結果：⚠️ 系統與論文真實存在，但46%/64%是特定亞組數字，非全體患者的「使用前後」對比**

「TiP DecScore」確實真實存在，並非自創或誤植的產品名。原始論文：發表於 *Communications Medicine*（Nature旗下期刊）2026年2月17日，第6卷，Article 165。全稱為「SGLT-2i/GLP-1RA Decision Score」，用機器學習（gradient boosting decision tree，15項臨床特徵）協助決定第2型糖尿病患者該用SGLT-2i還是GLP-1RA。訓練資料集來自「China Metabolic Analytics Project」，衍生資料集 n=24,322，驗證資料集 n=1,459。

**46.2% vs 64.1% 這組數字的真實語境**：這是**12個月時、「年齡<55歲」這個特定年齡亞組**中，「治療方式與TiP DecScore建議相符（concordant）」組別 HbA1c控制率64.1%，「不相符（discordant）」組別46.2%（P=0.001）——**不是「AI建議使用前後」的縱向對比，而是「用藥是否遵循AI建議」的橫向分組比較，且僅限於<55歲亞組**。全體患者的整體數字並非46%/64%（例如另一個對比是「GLP-1RA優於SGLT-2i」亞組在12個月時57.9% vs 28.6%）。

**結論**：「TiP DecScore」這個名稱是真的，不是幻覺產品名；但投影片把「特定年齡亞組、用藥符合度分組」的數字，簡化包裝成「使用AI建議後從46%提升到64%」的因果敘事，這種簡化容易被同行識破——正確說法應該是「在<55歲患者亞組中，用藥符合TiP DecScore建議者，HbA1c控制率（64.1%）顯著高於不符合者（46.2%）」。

**信心程度**：中高（系統名稱與數字真實，但因果框架與適用範圍被簡化/誤導）

---

## C. Agentic AI在肥胖/GLP-1真實世界研究的應用

### 8. 「MediKarma」的「Diabetes & Obesity Jill」功能，月活躍使用率35%

**查證結果：✅ 真實存在，數字吻合**

真實產品與新聞稿：MediKarma 於2026年1月宣布「Healthcare's First Agentic AI Licensing Model」，開放授權其已驗證的疾病管理AI代理人（agent）。其中「Diabetes & Obesity Jill」被明確描述為「a specialized agent for glucose and weight management」，新聞稿原文：「this agent drove 35% Monthly Active Users (MAU) – more than 4x the industry average – and achieved 40%+ improvement over baseline measures.」與投影片主張的「35%月活躍使用率」完全吻合。

**信心程度**：高

**來源**：PR Newswire / Yahoo Finance (2026年1月) "MediKarma Launches Healthcare's First 'Agentic AI' Licensing Model: Opens Access to Validated Disease Management Agents"

---

### 9. 「WeGoTogether」真實世界研究：Semaglutide 2.4mg，樣本數6964人以上，24個月平均減重-20.4%，50.5%達成≥20%減重

**查證結果：⚠️ 核心療效數字真實，但樣本數的呈現方式有誤導性**

真實研究：PubMed 40768192，"Real-World Weight Loss Among Patients Initiating Semaglutide 2.4 mg and Enrolled in WeGoTogether, a Digital Self-Support Application"（研究期間2021/6-2025/4）。

確認：**24個月平均減重-20.4%、50.5%患者達成≥20%減重，這兩個數字完全正確**。

**但樣本數的說法有問題**：研究**總納入人數是8,177人**，而「6,964」其實是**第6個月**時仍有體重資料可分析的人數（隨追蹤時間拉長，可分析人數持續遞減）。實際到**第24個月時，仍有體重資料的患者僅剩325人**（第12個月2,050人、第18個月491人、第24個月325人）。

**結論**：把「6,964人以上」講成是24個月追蹤結果所依據的樣本規模，會嚴重高估這組亮點數字的統計把握度——真正支撐「24個月-20.4%、50.5%達≥20%」這兩個數字的樣本只有325人，這是典型的**存活者偏誤（survivorship/attrition bias）**議題，在減重門診學術場合上台前應該明確揭露，否則容易被同行以「n只有325，你怎麼敢講50.5%」當場追問。

**信心程度**：中高（療效數字真實，但樣本規模表述具誤導性，需補充說明n隨時間遞減）

**來源**：PubMed 40768192；Journal of Endocrine Society SAT-694 abstract (academic.oup.com/jes)；ResearchGate/researchgate.net/publication/394354054

---

### 10. 「HealthVerity eXOs」與「streaMLine」真實世界證據平台

**查證結果：HealthVerity eXOs ✅ 真實存在；streaMLine ❌ 查無此事，疑似幻覺**

**HealthVerity eXOs**：真實存在。2025年9月正式發布，由 Medeloop 技術提供動力的對話式agentic AI平台，用於加速真實世界證據（RWE）研究設計與分析（HEOR、Medical Affairs、Commercial應用）。官方宣稱經過 ISPOR ELEVATE-GenAI框架驗證，250次執行測試中與已發表文獻高度一致、零幻覺（zero hallucinations）——不過這個「零幻覺」宣稱本身是廠商自我驗證研究的結論，屬於行銷/廠商白皮書性質，並非獨立第三方稽核，引用時建議註明此為廠商自評。

**streaMLine**：**多次以不同關鍵字組合搜尋（含IQVIA、Aetion、Certara、HealthVerity等可能廠商），都找不到任何名為「streaMLine」的真實世界證據平台或產品**。查到的相關但不同名的產品包括 IQVIA 的「IQVIA.ai」統一agentic AI平台（2026年3月發布）及與RWE無關的「SmartSolve RIM regulatory streamlining」工具（後者只是普通英文動詞streamline，非產品專名）。**「streaMLine」高度疑似是查證清單中最明確的一個幻覺案例**——名稱本身很可能是AI摘要工具自行拼湊或誤植的產物。

**信心程度**：HealthVerity eXOs 高；streaMLine 查無此事（疑似幻覺，信心程度：高）

**來源（HealthVerity eXOs）**：healthverity.com/exos/；PR Newswire (2025年9月)；PharmExec "Validating HealthVerity eXOs"

---

## D. 消費端體重管理平台

### 11. Noom平台聲稱透過AI介入使用者多減重25.2%（相較於沒有AI介入的對照）

**查證結果：⚠️ 數字真實存在，但「AI介入 vs 無AI介入」的框架描述不準確**

真實報告：Noom 於2026年2月4日發布的GLP-1參與度報告（Noom GLP-1 Engagement Report / Noom Companion program分析）。原文：「the most-engaged Noom GLP-1Rx Program members... lost 25.2% more weight, on average, by week 40, than the least-engaged members」（約多減重8.3磅），樣本數14,203名GLP-1Rx Program會員（另有30,239人用於藥物持續使用分析）。

**關鍵落差**：這是**「同一個AI驅動App內、高使用頻率 vs 低使用頻率」的四分位數比較**，**不是「有使用AI功能 vs 完全沒有AI介入」的對照組設計**——所有納入分析的會員都是Noom App的使用者（都暴露在同一套AI功能下），差異只在使用頻率高低。此外，Noom官方報告本身**明確聲明這是觀察性分析，不是隨機對照試驗**，原文：「These findings reflect observational analyses and report associations/correlations, not proof that engagement causes improved outcomes.」——也就是說Noom自己都承認這只是相關性，不能推論因果（不能說是「AI介入造成」多減重25.2%）。

**結論**：25.2%這個數字真實可查，但投影片若把它包裝成「AI介入 vs 無AI介入」的對照效果，混淆了「使用頻率高低」與「有無AI」兩件事，且忽略了Noom官方自己強調的「非因果、僅相關性」但書。上台被同行追問「這是RCT還是觀察性研究？」時容易站不住腳。

**信心程度**：中高（數字真實，但因果框架需要修正措辭）

**來源**：noom.com/in-the-news/people-who-use-noom-the-most-also-lose-the-most-weight/（2026年2月）

---

## 總結

### 查證結果總覽

| # | 主張 | 判定 | 信心 |
|---|---|---|---|
| 1 | Semaglutide 7.8% vs 9.5%（AI參與） | ⚠️ 語境嫁接 | 中 |
| 2 | Tirzepatide 11.2% vs 13.9%（AI參與） | ⚠️ 語境嫁接 | 中 |
| 3 | GLP-1市場 385億→1300億（GVR/PwC/JPM） | ⚠️ 來源誤植 | 低 |
| 4 | Mayo/Phenomix GRS 噁心68% vs 30% | ✅ 真實（需註明liraglutide、n=110） | 高 |
| 5 | Nomogram AUC 0.84-0.86 | ⚠️ 數字真實但研究張冠李戴 | 中 |
| 6 | PrecisionLife/Ovation 準確率95%/PPV96% | ⚠️ 骨架真實，效能數字查無出處 | 中 |
| 7 | TiP DecScore HbA1c 46%→64% | ⚠️ 系統真實，數字為特定亞組被簡化 | 中高 |
| 8 | MediKarma「Jill」MAU 35% | ✅ 真實吻合 | 高 |
| 9 | WeGoTogether n≥6964、24月-20.4%、50.5% | ⚠️ 療效數字真實，樣本數表述誤導 | 中高 |
| 10a | HealthVerity eXOs | ✅ 真實存在 | 高 |
| 10b | streaMLine | ❌ 查無此事，疑似幻覺 | 高 |
| 11 | Noom AI介入多減重25.2% | ⚠️ 數字真實，因果框架描述不準確 | 中高 |

### 整體評估

這批2026年素材呈現出非常一致的模式：**幾乎沒有一條是「完全憑空捏造」的純幻覺數字**（唯一明確查無出處的是 #10b「streaMLine」），但**絕大多數（8/11）都存在「真數字、假語境」的問題**——也就是AI搜尋/摘要工具從真實文獻中撈出正確的數字，卻把它們錯誤地重新配對、跨研究拼接、或簡化成過度乾淨俐落的因果敘事。具體來說：

- **主張1、2**是最嚴重的問題：把同一篇論文中「semaglutide vs tirzepatide藥物間比較」的數字（9.5%、13.9%），錯貼成「AI參與 vs 未參與」的對照組數字，且配對的另一半數字（7.8%、11.2%）完全查無出處——這兩條**建議直接刪除，不要用於正式演講**，因為只要同行去查JMIR e69466原文，會立刻發現這是誤讀。
- **主張3**的三個標注來源（GVR/PwC/JPM）沒有一個真的發表過385億/1300億這組數字，J.P. Morgan公開數字甚至與投影片方向相反（$200B）——**建議整條改用可驗證的單一來源**（例如直接引用DelveInsight的$38.5B或UBS的$130B，並各自標明正確機構），不要沿用現有的來源標注。
- **主張5**的AUC數字其實屬於另一篇跟基因檢測完全無關的論文，若要用，**必須換成正確作者（Gao et al., Frontiers in Endocrinology 2024）**，不能掛在Mayo/Phenomix名下。
- **主張6、9**的核心骨架是真的，但各自少了一個關鍵數字的出處（PrecisionLife的準確率/PPV）或誇大了樣本規模（WeGoTogether的24個月n其實只有325）——**可以用，但務必附加正確的限定條件**，否則現場被問到細節會站不住腳。
- **主張4、8、10a、11**是這批素材中相對最站得住腳的部分：核心數字都能在真實新聞稿或論文中直接對應，只是主張11在「因果 vs 相關性」的措辭上需要修正（Noom官方自己都聲明是觀察性分析）。
- **主張7**的系統名稱「TiP DecScore」不是幻覺，是真實存在的臨床決策工具，只是投影片把亞組分析簡化成了全體適用的敘事。

**給使用者的建議**：這批素材**不宜整批直接搬上台**，但也不必整批捨棄。建議做法：
1. **直接刪除**主張1、2（AI參與度 vs 藥物比較混淆，風險最高）。
2. **刪除或替換**主張10b「streaMLine」（查無此產品）。
3. **主張3、5**若要保留，務必更換為查證後的正確來源與機構名稱，不要沿用投影片現有標注。
4. **主張4、6、7、8、9、11**可以使用，但每一條都要在投影片註腳或口頭補充中加上查證出的限定條件（藥物別、樣本數、亞組範圍、觀察性研究性質等），才經得起現場同行追問。

換言之：這不是「整批AI生成的示意內容、應該整批不用」，而是「每條主張的核心數字大多有真實出處，但AI彙整過程中發生了系統性的語境錯置與過度簡化」——**上台前每一條都需要回到原始文獻重新核對措辭，不能直接照抄投影片現有文字**。
