# P12 出處補查報告：GLP-1 藥物與 AI 結合的進展（一）

**查證日期**：2026-09-16（演講 2026-09-20）
**查證對象**：P12 三個標記 [1] GRS 卡、[2] TiP DecScore 卡、[3] 結論句
**查證方法**：三個 subagent 平行查 PubMed／Europe PMC／Crossref／OpenAlex／ClinicalTrials.gov／官方新聞稿與政策文件，逐條讀到一手來源
**前置**：接續 `citation-verification.md`（2026-08-14）主張 4 與主張 7；本檔只補缺口，不重複

---

## 0. 投影片改字總表（先看這個）

| 位置 | 現況 | 問題 | 建議 |
|---|---|---|---|
| [1] 卡標題 | 基因風險分數（GRS）預測藥物反應 | 數字講的是**副作用**不是療效；且同一分數在療效與副作用方向相反（低 GRS 減重較好、高 GRS 噁心較多），「藥物反應」會讓人以為高 GRS＝反應好 | 「CTS-GRS 預測 GLP-1 噁心風險（探索性）」 |
| [1] 註腳 n=110 | liraglutide，n=110 | 110 是**有基因資料的總人數（含安慰劑組）**；68%/30% 只在 liraglutide 組（完成者 59 人）內比較，每格事件數推估約 9–17 人 | 「n=110（有基因資料）；噁心比較限 liraglutide 組」，並依小樣本原則不放亮點位置 |
| [1] 註腳來源 | Mayo Clinic／Phenomix｜會議摘要層級 | 缺正式引用；「會議摘要層級」正確且**必須保留**（截至 2026-09-16 未見全文） | Fredrick TW, et al. *Gastroenterology* 2025;169(1 Suppl):S-946–S-947（DDW 2025 Su2057） |
| [1] 數字 | 68% vs 30% | 正確，與一手摘要相符 | 可補 OR 5.0、p=0.0058（原文未報 95% CI） |
| [2] 卡標題 | TiP DecScore：用藥是否符合 AI 建議 | 回溯資料事後分類，醫師開藥時模型不存在；論文全文未用 "AI"，只用 machine learning | 「TiP DecScore：處方恰與模型建議一致 vs 不一致（回溯分析）」 |
| [2] 數字 | HbA1c 控制率 64.1% vs 46.2% | 數字正確，但缺「HbA1c <7%」「12 個月」 | 「12 個月 HbA1c <7% 達標率 64.1% vs 46.2%」 |
| [2] 標籤 | 僅 <55 歲亞組 | 「僅」字反效果——**全體世代 6、12 個月都顯著**（12 個月 55.1% vs 47.4%，P=0.028）；反而是 ≥55 歲與女性 12 個月時反轉不顯著 | 「<55 歲亞組（全體 55.1% vs 47.4%，P=0.028）」，至少拿掉「僅」 |
| [2] 註腳來源 | Communications Medicine 2026 | 無法回溯 | Shi J, et al. *Commun Med* 2026;6:165, Fig. 3C |
| [3] 結論句 | 用 AI 挑對病人——把有限的藥物資源配置到最可能受益的人 | 語意可保留，但同行有三個現成反駁（見 §3.5）；現行政策（NHS／NICE／Medicare）是按**臨床需求**配置，不是按「誰會減最多」 | 口頭加保留語（見 §3.7 講稿） |

另：`citation-verification.md` 主張 7 段落中「GLP-1RA 優於 SGLT-2i 亞組 57.9% vs 28.6%」為**誤讀**——原句是模型建議 GLP-1RA／SGLT-2i 的**病人比例**（另 13.5% 不給建議），不是療效對比。P12 目前沒用到這組數字，備忘稿要留意。（2026-09-16 已在該舊檔主張 4、主張 7 段落下各補一則引用區塊註記；本表建議已於同日套用至 `slides/index.html` 與 `slides/spec.yaml` P12。）

---

## 1. [1] Mayo Clinic／Phenomix CTS-GRS 預測 liraglutide 噁心

### 1.1 正式引用（一手：Crossref metadata ＋ DDW ePoster Library）

> Fredrick TW, Atieh J, Maselli DB, Anazco D, Cifuentes L, Espinosa MA, Villamarin JL, Eckert DJ, Ciotlos S, O'Connor TR, Camilleri M, Acosta A. Su2057: A Genetic Risk Score Associated with Nausea Resulting from GLP-1 **Receptor** Agonist Treatment: A Post-Hoc Analysis of a Randomized Controlled Trial of Liraglutide. *Gastroenterology*. 2025;169(1 Suppl):S-946–S-947. doi:10.1016/S0016-5085(25)03109-9

- 發表：2025-05-04，DDW 2025，AGA／Obesity and Nutrition track，**Posters of Distinction 2025**
- 摘要全文頁：https://eposters.ddw.org/ddw/2025/ddw-2025/4156209/thomas.fredrick.a.genetic.risk.score.associated.with.nausea.resulting.from.html
- Crossref：https://api.crossref.org/works/10.1016/s0016-5085(25)03109-9 ｜ OpenAlex W4411982091（conference-abstract）
- 注意：8/14 記錄的標題少了 "Receptor"；「1 Suppl」係依 Crossref `special_numbering="S"` 推定（期刊站 403 未能親眼確認），保守寫法 `2025;169(1):S-946–S-947` 亦對得上

### 1.2 全文發表狀態：截至 2026-09-16 **未查到**

PubMed（Fredrick TW 全部著作）、Europe PMC（含 preprint）、Crossref 2026 增刊掃描、OpenAlex／Semantic Scholar 引用追蹤——皆無此研究的全文論文，同團隊未擴寫。**「會議摘要層級」標示正確，必須保留。**

同一 GRS 的主論文已發表，但**只有減重療效終點、不含噁心**：
> Cifuentes L, Anazco D, O'Connor T, …, Camilleri M, Acosta A. Genetic and physiological insights into satiation variability predict responses to obesity treatment. *Cell Metab*. 2025;37(8):1655-1666.e5. doi:10.1016/j.cmet.2025.05.008（PMID 40482646）
> — 獨立 liraglutide RCT（n=110 有基因資料，**即本摘要同一世代**）：低 CTS-GRS 16 週 −6.4±0.7% vs 高 −3.3±0.8%（p=0.0005）；預測「高 CTS」AUC 0.69（0.59–0.80）

### 1.3 研究細節

| 項目 | 內容 | 來源 |
|---|---|---|
| 母試驗 | NCT03523273「Pilot Study of the Effect of Liraglutide 3.0 mg on Weight Loss and Gastric Functions in Obesity」，Mayo Rochester 單中心、雙盲、安慰劑對照、Phase 2；Maselli D, et al. *Obesity* 2022;30(8):1608-1620. doi:10.1002/oby.23481 | ClinicalTrials.gov；PubMed 35894080 |
| 劑量／期間 | liraglutide 0.6→3.0 mg/日（約 4 週達標），共 16 週 | 母試驗論文 |
| 樣本 | 136 隨機 → 124 完成（liraglutide 59、placebo 65）；BMI >30、18–65 歲；排除本來就胃排空延遲者；**110 人有基因資料** | 母試驗＋摘要 |
| 母試驗主要終點 | 固體胃排空 T½（非減重）；噁心屬安全性項目；母試驗噁心率 liraglutide 59.7% vs placebo 15.9%；**有噁心者減重較多**（4.7 vs 1.8 kg，p=0.044） | 母試驗論文 |
| GRS 組成 | 10 基因：SIM1、PCSK1、SH2B1、LEPR、UCP2、FTO、TNFRSF11A、ADRA2A ＋ GLP1R ＋ TCF7L2；SVC 輸出「高 CTS 機率」>0.5 判高 | Cell Metab 方法段 |
| 主結果 | liraglutide 組：高 GRS 噁心 **68%** vs 低 GRS **30%**，**OR 5.0，p=0.0058**；placebo 組 19% vs 13%（p=0.5562） | 摘要原文 |
| 其他終點 | 頭痛 OR 5.4（p=0.0096）；整體 GI 副作用 73% vs 53%（摘要稱 trend，未給 p）；因噁心退出兩組各 2 人；噁心與 5／16 週 TBWL 無關；胃排空、胃容受、熱量攝取無差異 | 摘要原文 |
| 摘要未報告 | 95% CI、AUC、各組人數、嘔吐單獨終點 | — |

**分母問題（subagent 反推，非文獻數字）**：同時滿足 68%／30%／OR 5.0／p=0.0058 的組合約落在高 GRS 19–38 人、低 GRS 13–30 人，最貼合解為 17/25 vs 9/30。結論穩固：**每格事件數約 9–17**，屬小樣本亞組。

**OR 5.0／p=0.0058 怎麼解讀（備忘稿用）**：
- OR（勝算比）5.0 是「噁心的勝算」相除：高 GRS 組 0.68/0.32≈2.1，低 GRS 組 0.30/0.70≈0.43，2.1/0.43≈5.0。
- **不要講成「風險 5 倍」**。噁心是常見事件（68%），OR 會誇大；直接看比例是 68/30≈**2.3 倍**，新聞稿原句也是 "more than twice as likely"。投影片上兩個百分比都在，聽眾自己會算出 2.3 倍，若口頭說 5 倍會被質疑。
- p=0.0058（卡方檢定）：若兩組真的沒差，出現這麼大差距的機率約 0.6%，達傳統顯著。但這是 post-hoc 探索性分析、同時看了噁心／頭痛／整體 GI 等多個終點、未做多重比較校正，且摘要沒報 95% CI。
- 以反推的 17/25 vs 9/30 估算（**非文獻數字，僅示意**），OR 的 95% CI 約 1.6–16：下限離 1 不遠、上限極寬，代表「方向可信、大小不可信」。
- 支持「藥物–基因交互作用」而非「高 GRS 的人本來就容易噁心」的證據，是安慰劑組沒差（19% vs 13%，p=0.56）；但摘要沒有正式檢定交互作用項。

**內部矛盾備忘**：母試驗說有噁心者減重較多（p=0.044），本摘要說噁心與 TBWL 無關（分析方式不同：kg vs %、全體 vs 分層）。Q&A 若被問「噁心是不是代表有效」要知道這點。

### 1.4 與 Phenomix 商品的關係

- **同一分數**：CTS-GRS 即 MyPhenome 核心；官方對應 低 CTS-GRS＝Hungry Gut、高＝Hungry Brain（PR Newswire 2025-06-10）
- **副作用預測未商品化**：Mayo 官方新聞 2025-09-17 稱仍在 "developing models to predict common side effects such as nausea and vomiting"；產業報導 2026-04-08 稱 Phenomix "is developing a test to identify 'super intolerant' patients"
- MyPhenome 商品化的是**療效配對**（唾液檢測；2025-11 稱近 400 家診所）；FDA／CLIA 狀態與價格未公開
- 前瞻試驗 PhenoRX（NCT07728812，n=424，2026-09 預計開始）與 Mayo NCT06814938（semaglutide，n=135）**都只看體重，不看耐受性**
- 利益衝突：Acosta、Camilleri 與 Mayo Clinic 為授權給 Phenomix 之專利發明人；Su2057 作者含 Phenomix 員工 2 人（Ciotlos、O'Connor）

### 1.5 外推到 semaglutide／tirzepatide：**噁心終點無任何外推資料**

- 療效面外推有但分歧：ADA 2024 摘要 234-OR（*Diabetes* 2024;73(Suppl 1)，doi:10.2337/db24-234-or，n=137）該分數對 semaglutide 有預測力（AUC 0.7，CI 0.5–0.9，p=0.06）、**tirzepatide 沒有**
- 若要講針劑世代的噁心基因學，改引同行審查全文：
  > Su QJ, Ashenhurst JR, …, Auton A. Genetic predictors of GLP1 receptor agonist weight loss and side effects. *Nature*. 2026;653(8115):770-775. doi:10.1038/s41586-026-10330-z（PMID 41951734）
  > — 23andMe n=27,885（自述資料，78.3% 歐洲血統）；GLP1R 變異噁心 OR 1.36、嘔吐 OR 1.57；GIPR p.Glu354Gln 嘔吐 OR 1.83 **僅見於 tirzepatide**；噁心預測 AUC 0.654、嘔吐 0.680；效應等位基因頻率**東亞 16% vs 歐洲 40%**，亞洲族群未達顯著

### 1.6 批評與限制

- Cell Metab 邀稿評論：Edwin Thanarajah S, et al. Calories to satiation—A new predictor of anti-obesity therapy outcome? *Cell Metab*. 2025;37(8):1628-1629. doi:10.1016/j.cmet.2025.07.003（標題即問號；全文 403，僅摘要）
- Cell Metab 主論文自陳：liraglutide 部分為 post-hoc；>20% 非歐洲血統樣本被剔除；呼籲前瞻 RCT 驗證
- 本摘要特有：post-hoc、單藥、單中心、16 週、樣本小、無 CI、**分數原為 satiation／療效設計，拿來看副作用屬探索性**
- Kuryłowicz A, Czupryniak L. *Diabetes Obes Metab* 2026. doi:10.1111/dom.71226：即使 Nature GWAS 仍屬 "self-reported, single-cohort and as-yet unreplicated"，只能視為產生假說

### 1.7 建議註腳寫法

最小改動版：
> Fredrick TW, et al. *Gastroenterology* 2025;169(1 Suppl):S-946–S-947（DDW 2025 Su2057）｜Mayo Clinic／Phenomix｜liraglutide 3 mg × 16 週 post-hoc；有基因資料 n=110，噁心比較限 liraglutide 組｜高 vs 低 CTS-GRS 68% vs 30%，OR 5.0，p=0.0058（未報 CI）｜會議摘要層級，截至 2026-09 未見全文

可加兩行（版面允許時）：
> CTS-GRS 為 10 基因（含 GLP1R、TCF7L2）ML 分數，原為預測 satiation／療效而建；安慰劑組無此差異（19% vs 13%，p=0.56）
> 利益衝突：Mayo／Acosta、Camilleri 為授權 Phenomix 之專利發明人，作者含 Phenomix 員工

### 1.8 查不到（不猜）

高／低組實際人數與事件數（Table 在 ePoster 圖檔需 DDW 帳號）；95% CI；噁心預測 AUC；GI 副作用 p 值；嘔吐單獨數字；Cell Metab 評論內文；增刊在官網的確切標示；SSRN semaglutide 預印本（abstract_id 5961920）是否已正式發表；MyPhenome 法規狀態與價格。

---

## 2. [2] TiP DecScore（Commun Med 2026）

### 2.1 完整引用（PubMed、Europe PMC JATS XML、OpenAlex 三方一致）

> Shi J, Liu C, Hu J, Dai Y, Peng Y, Xu F, et al. A machine learning model for optimizing treatment of patients with poorly controlled type 2 diabetes. *Commun Med*. 2026;6:165. doi:10.1038/s43856-026-01442-8（PMID 41703087；PMC13022273）

- Received 2025-04-10；Accepted 2026-02-04；Published **2026-02-17**；Gold OA，CC BY-NC-ND 4.0
- 30 位作者；共同第一作者 6 位；通訊作者 Yufan Wang、Zhiyun Zhao、Yifei Zhang、Weiqing Wang（lead contact）；資深作者含 Guang Ning
- 機構：上海交大醫學院附屬瑞金醫院內分泌代謝科；驗證資料來自 Shanghai regional referral system
- PMC 全文：https://pmc.ncbi.nlm.nih.gov/articles/PMC13022273/ ｜ 補充資料：https://static-content.springer.com/esm/art%3A10.1038%2Fs43856-026-01442-8/MediaObjects/43856_2026_1442_MOESM1_ESM.pdf

8/14 記錄的「6:165、2026-02-17」正確。

### 2.2 64.1% vs 46.2% 精確語境

| 項目 | 查證結果 | 位置 |
|---|---|---|
| 出處 | 正文 Fig. 3C（12 個月）＋ Results「Model application」段 | "64.1% in younger patients, whereas it was 46.2% in the discordant group (P = 0.001)" |
| 時間點 | 12 個月（取 7–15 個月內最接近一筆） | Methods |
| 「控制」定義 | HbA1c **<7%（<53 mmol/mol）** | Methods；Fig. 3 X 軸 |
| P 值 | 0.001，多變項 logistic regression 調整後（年齡、病程、HbA1c、FBG、BMI、DBP…） | Methods |
| 百分比性質 | 原始比例（未調整），誤差線 SE | Fig. 3 圖說 |
| 調整後 OR／CI | **未報告** | — |
| <55 歲亞組 n | **未報告**；12 個月驗證世代 n=829（SGLT-2i 623、GLP-1RA 206），平均年齡 52.6±12.7 | Supp. Table 2 |
| concordant／discordant 各幾人 | **未報告**（全體與各亞組皆無） | — |
| 分組定義 | 以模型建議為基準看實際處方是否吻合；分數在 ±0.1 之間「不給建議」者不進入比較 | Fig. 3A |

### 2.3 全體世代與所有亞組（Fig. 3B/3C 完整轉錄；P 為調整後）

| 亞組 | 6 月 concordant | 6 月 discordant | P | 12 月 concordant | 12 月 discordant | P |
|---|---|---|---|---|---|---|
| **全體** | 57.4% | 49.4% | **0.006** | 55.1% | 47.4% | **0.028** |
| <55 歲 | 66.3% | 58.1% | 0.044 | **64.1%** | **46.2%** | **0.001** |
| ≥55 歲 | 49.6% | 41.7% | 0.040 | 46.8% | 48.5%（反轉） | 0.495 |
| 男性 | 59.9% | 53.4% | 0.076 | 58.6% | 45.6% | 0.018 |
| 女性 | 52.5% | 43.9% | 0.032 | 49.2% | 51.2%（反轉） | 0.348 |

- 只有年齡與性別兩種亞組；**無** BMI、基線 HbA1c、病程亞組
- 藥物亞型（Supp. Fig. 13）：Dapagliflozin/Liraglutide 使用者 12 月 53.19% vs 48.24%（P=0.164）；Dapagliflozin/Semaglutide 53.58% vs 42.55%（P=0.019）
- 作者 Discussion："when applying the model to older patients and females, clinicians should integrate assessments of comorbidities"
- **判讀**：全體顯著、<55 歲與男性更明顯、≥55 歲與女性 12 個月消失甚至反轉。投影片挑 64.1% vs 46.2% 是最漂亮的一格，可以，但註腳要讓聽眾知道全體是 55.1% vs 47.4%
- 模型 AUC 0.71–0.78

### 2.4 研究設計

- **回溯性觀察資料**（ChinaMAP／MMC 隨訪資料庫；衍生 2017-06～2023-12，驗證 2017-06～2024-07）；依 STROBE
- **醫師沒看過分數**：分數事後算出再分類 concordant／discordant；驗證世代處方最晚 2024-07，論文 2025-04 投稿。作者用詞 "receiving the predicted optimal therapy"，非「依建議用藥」
- 無介入、無 RCT、無前瞻 implementation study；NCT03811470 是 MMC 母計畫登錄
- Discussion 宣稱模型已在上海轉診系統應用並改善結果——**無數據無引用**
- 結局是 **HbA1c**，對象是**控制不佳的 T2DM**，不是體重、不是減重門診族群

### 2.5 「TiP」、AI 稱謂、工具可用性

- 「TiP」展開：正文、補充資料、GitHub README 皆未定義；**投影片不要自行展開**
- 模型：gradient boosting decision tree（scikit-learn／LightGBM／XGBoost）；全文未用 "AI"；建議投影片寫「機器學習模型（GBDT）」
- 線上工具：**沒有**。https://liucong2020.github.io/TiP-DecScore/ 只有一個 notebook 連結，模型檔與資料檔未公開，外人無法執行；notebook 門檻 0.15 與論文 ±0.1 不一致

### 2.6 資金、COI、驗證、後續

- 資金全為政府／學術（2023ZD0508100、NSFC 82270896／82470932、SHDC22022301 等），無藥廠；"no competing interests"（作者 Weiwei Tu 隸屬公司 "Artificial Productivity, Beijing"）
- **無中國以外外部驗證**；作者自承 validation dataset relatively small
- 無 commentary／editorial／letter；Europe PMC／OpenAlex 被引 0，Semantic Scholar 1（低能見度綜述）
- 對照研究（非延伸）：Mori T, et al. *Exp Clin Endocrinol Diabetes* 2026;134:79-87. doi:10.1055/a-2798-6496 — 德國／奧地利 DPV 登錄評估另一套 GLP-1RA vs SGLT2i 個人化演算法（ASCVD 結局），**未顯示益處**（HR 0.88, 95% CI 0.64–1.21）。Q&A 可用作平衡觀點

### 2.7 論文內部不一致（供避開）

- 驗證世代 n=1,459，但同段 1,088+421=1,509、960+548=1,508；差 50 人未解釋。引 n 時建議用 12 個月的 829（Supp. Table 2 自洽）
- 衍生世代 GLP-1RA 使用者達標率剛好也是 46.2%（vs SGLT-2i 37.1%），與 discordant 46.2% 是不同數字，Q&A 別混

### 2.8 建議註腳寫法

參考文獻頁：
> Shi J, Liu C, Hu J, et al. A machine learning model for optimizing treatment of patients with poorly controlled type 2 diabetes. *Commun Med.* 2026;6:165. doi:10.1038/s43856-026-01442-8

投影片短版：
> Shi J, et al. *Commun Med* 2026;6:165, Fig. 3C｜回溯驗證世代（上海，12 個月 n=829）｜HbA1c <7% 達標率，<55 歲亞組，調整後 P=0.001；全體 55.1% vs 47.4%（P=0.028）

口頭補：「這是回溯關聯，醫師開藥時沒看過分數，尚無前瞻驗證；結局是血糖不是體重。」

### 2.9 查不到（不猜）

<55 歲亞組 n；各亞組 concordant／discordant 人數；調整後 OR／CI；「TiP」展開；上海應用成效數據；任何評論；任何外部驗證或延伸研究。

---

## 3. [3] 結論句「用 AI 挑對病人」的佐證與反方

### 3.1 先講三個會影響講法的發現

1. **Acosta 2021 的 15.9% vs 9.0% 不是隨機試驗。** *Obesity* 2021;29:662-671（doi:10.1002/oby.23120）於 2021-09 刊更正啟事（*Obesity* 2021;29:1565-1566，doi:10.1002/oby.23236）：未在 ClinicalTrials.gov 註冊、**沒有隨機分派**、研究者未盲化、部分治療醫師即研究者，"best described as an observational comparison of two convenience samples"。摘要的 "randomly assigned" 是錯的。
2. **Mayo 真正的隨機三盲試驗結果幾乎沒差，且未發表。** NCT03374956（n=193，完成 2022-05-26，結果貼於 ClinicalTrials.gov 2023-07-18）：12 週體重中位數 −7.7%（表型導向）vs −6.5%（隨機指定）；≥5% 反應者 **81% vs 80%**；≥10% 44% vs 40%。PubMed 查無期刊論文。
3. **支持方最強的同行審查證據是 Cifuentes/Acosta, *Cell Metab* 2025**（見 §1.2）：低 CTS-GRS liraglutide −6.4% vs −3.3%（p=0.0005）；但獨立驗證 AUC 0.69–0.75，Phenomix 員工為共同作者。

### 3.2 A. GLP-1／tirzepatide 反應異質性（「需要挑病人」的前提）

| 來源 | 關鍵數字 | 層級 |
|---|---|---|
| Wilding JPH, et al. STEP 1. *NEJM* 2021;384:989-1002. doi:10.1056/NEJMoa2032183 | n=1,961；68 週 −14.9% vs −2.4%；達 ≥5% 86.4%（→ **13.6% 未達**，treatment-policy）；≥10% 69.1%；≥15% 50.5% | RCT |
| Jastreboff AM, et al. SURMOUNT-1. *NEJM* 2022;387:205-216. doi:10.1056/NEJMoa2206038 | n=2,539；72 週 5/10/15 mg 達 ≥5% 85%/89%/91%（→ **9–15% 未達**） | RCT |
| Ard J, et al. *Diabetes Obes Metab* 2025;27:5064-5071. doi:10.1111/dom.16554 | SURMOUNT-1 post hoc n=1,545；12 週未達 5% 者 18%，其中 **70% 在 24 週、90% 在 72 週達 ≥5%** | RCT 事後（Lilly 資助） |
| Kuryłowicz A, Czupryniak L. *Diabetes Obes Metab* 2026. doi:10.1111/dom.71226 | "non-response… approximately 10% of participants in controlled trials, with real-world cohorts suggesting a higher frequency"；**"No single baseline characteristic reliably predicts response"** | 敘述性回顧 |
| Rodriguez PJ, et al. *JAMA Intern Med* 2024;184:1056-1064. doi:10.1001/jamainternmed.2024.2525（Truveta EHR） | 配對 n=18,386；1 年達 ≥5%（on-treatment）tirzepatide 81.8% vs semaglutide 66.5%（→ 18%／**33.5% 未達**）；停藥率 55.9%／52.5% | 真實世界回溯 |
| Gasoyan H, et al. *Obesity* 2025;33:1657-1667. doi:10.1002/oby.24331 | n=7,881；1 年 −8.7%；80.8% 停在低維持劑量 | 真實世界回溯 |
| Gasoyan H, et al. *Obesity* 2025;33:2296-2303. doi:10.1002/oby.70058 | 停藥原因：**費用／保險 47.6%**、副作用 14.6%、缺貨 11.8%、減重不滿意 **1.7%** | 病歷審查 |
| Venkatakrishnan AJ, et al. *PNAS Nexus* 2026. doi:10.1093/pnasnexus/pgag171 | 配對 10,339 對；1 年 ≥15%：tirzepatide 42.6% vs semaglutide 21.6%；Black／Hispanic 在 <5% 組被高估代表 | 真實世界回溯 |

**用法**：「試驗約 1 成、真實世界約 3 成的 semaglutide 使用者一年減不到 5%」——但要補：真實世界的無反應大半是停藥、低劑量、費用，不是生物學無反應。

### 3.3 B. 表型／基因導向選藥的證據

- **Acosta 2021**（見 §3.1）：表型導向 n=84 vs 非導向 n=228；12 個月 −15.9% vs −9.0%（差 −6.9%，CI −9.4 至 −4.5）；>10% 者 79% vs 34%；<5% 者 2% vs 26%；校正後 −13.6% vs −6.6%；基線不平衡（導向組較年輕 7.2 歲）；Phenomix 授權與持股。**引用時註腳必須寫「非隨機、觀察性；作者自行更正」**
- **Cell Metab 2025**（§1.2）：phentermine-topiramate 52 週高 CTS-GRS −17.4% vs 低 −11.2%（p=0.01）；liraglutide 16 週低 −6.4% vs 高 −3.3%
- **DDW 2024 Abstract 638**（semaglutide n=84；Hungry Gut 陽性 51／陰性 33；12 個月 19.5% vs 10% TBWL）：會議摘要＋新聞稿，PubMed 無全文
- **ObesityWeek 2025**（Phenomix 新聞稿 2025-11-04）：多族裔 n=158 12 個月 9.6% vs 4.4%（p=0.002）：新聞稿層級
- **Ticho AL, et al. *Gastroenterology* 2026. doi:10.1053/j.gastro.2026.05.019**：483 人分群，「胃排空快＋餐後 GLP-1 偏低」亞型（26.9%）tirzepatide 6 個月 21.5% vs 11.7%（n=61，回溯）
- **Su QJ, et al. *Nature* 2026;653:770-775**（§1.5）：GLP1R p.Pro7Leu 每等位基因多減 0.76 kg（CI −1.27 至 −0.34）；All of Us 重現、UK Biobank 未重現；整合模型只解釋 25% 變異且主要來自非基因因素
- **不建議引用**：Abegaz TM, Frietze G. *Front Artif Intell* 2026. doi:10.3389/frai.2026.1861563（AUC 0.94 但結局「追蹤時 BMI<30」被基線 BMI 洩漏，僅內部驗證）——可當反面教材
- Helix medRxiv 2024.10.31.24316494（BMI 多基因分數低者反而減得多）：預印本

### 3.4 C. 「藥物資源有限」的官方事實

| 項目 | 事實 | 層級 |
|---|---|---|
| NICE TA1026（2024-12-23） | tirzepatide 用於 BMI ≥35 ＋ ≥1 共病（亞裔 BMI 門檻減 2.5）；6 個月減 <5% 應重新評估 | HTA 指引 |
| NHS England Interim commissioning guidance（2025-03-27） | NICE 估 **340 萬人**符合；NHS 只規劃**前 3 年 22 萬人**、最長 **12 年**分批；基層自 2025-06-23 起；第 1 年只給 **BMI ≥40 且 5 項共病中 ≥4 項**；理由 "system capacity, workforce readiness, and resource availability" | 政策文件 |
| 美國 Medicare 法定排除 | SSA §1860D-2(e)(2)(A) 自 Part D 開辦即排除減重用途（KFF 2026-05-11） | 法規 |
| Medicare GLP-1 Bridge（CMS Fact Sheet 12234，2026-06） | 2026-07-01～2027-12-31，自付 $50/月；BMI ≥35，或 ≥30＋特定共病，或 ≥27＋糖尿病前期／曾 MI 等 | 官方文件 |
| CMS BALANCE Model | 2025-12-23 宣布；Medicaid 2026-05 起；Part D 部分 2026-04-21 無限期延後 | 官方／KFF |
| 2025-11-06 Lilly／Novo 協議 | Medicare/Medicaid 淨價 $245/月 | 新聞 |
| FDA 缺藥 | tirzepatide 2022-12-15 列缺藥，2024-12-19 確認解除；semaglutide 2025-02-21 解除 | FDA |
| 台灣食藥署 2025-11-10 | 2025-09 禮來通報部分劑量控貨，10 月恢復 | 官方新聞稿 |
| 台灣健保 | GLP-1RA 僅限 T2DM（HbA1c >8.5% 等條件）；減重適應症全自費 | **醫院／基金會衛教，非健保署新聞稿** |

### 3.5 D. 反方（同行可能怎麼反駁）

1. 「表型導向研究不是 RCT，真正的 RCT 幾乎沒差」（§3.1 第 1、2 點）——最尖銳
2. 「沒有任何基線特徵能可靠預測反應」——Kuryłowicz 2026；Lopez Delgado, et al. *Front Med* 2026. doi:10.3389/fmed.2026.1803474："remain investigational and require prospective, multi-ancestry validation"
3. 「早期無反應者多數後來會反應」——Ard 2025：90% 在 72 週達標；用 AI／早期反應停藥會錯殺
4. 「基因解釋的變異很小，且東亞頻率低」——Nature 2026；Krieger JE. *Front Cardiovasc Med* 2026. doi:10.3389/fcvm.2026.1870807
5. 「外部驗證差／方法洩漏」——Cell Metab AUC 0.85→0.69；Front AI 2026 洩漏；Phenomix 多為摘要＋新聞稿；Mayo 與 Phenomix 授權持股
6. 「個體反應差異有多少是真的」——Williamson PJ, et al. *Obes Rev* 2018;19:960-975. doi:10.1111/obr.12682（運動 RCT 真實個體反應 SD 僅 0.8 kg；GLP-1 尚無同類分析）
7. 「AI 配置有限資源會加深不平等」——Shah N, et al. *J Gen Intern Med* 2026;41:2859-2872. doi:10.1007/s11606-026-10178-z（26 篇 >1,460 萬人；低 SES aOR 0.73、Medicaid 0.70、**亞裔 0.49**、黑人 0.80）；Mallette, et al. *Obesity* 2026. doi:10.1002/oby.70180（黑人 −4.9% vs 白人 −7.1%）；Ahmed MM, et al. *Ther Adv Endocrinol Metab* 2026. doi:10.1177/20420188261472587；Obermeyer Z, et al. *Science* 2019;366:447-453. doi:10.1126/science.aax2342
8. 「現行配置是按臨床需求（BMI＋共病），不是按預測反應」——NHS／NICE／Medicare Bridge 皆然；「受益」的定義是減重幅度還是心血管風險？

### 3.6 前 5 名最值得放註腳／備忘稿

1. Cifuentes L, …, Acosta A. *Cell Metab* 2025;37:1655-1666.e5 — 支持方最強；備忘稿寫 AUC 0.69 與 Phenomix 作者關係
2. Acosta 2021 *Obesity* 29:662 ＋ 更正啟事 29:1565 ＋ NCT03374956 — 引 15.9% vs 9.0% 的前提是知道它非隨機、RCT 不同
3. Su QJ, et al. *Nature* 2026;653:770-775 — 基因影響反應與副作用的最高層級證據，但效應小、東亞頻率低
4. Kuryłowicz A, Czupryniak L. *Diabetes Obes Metab* 2026 — 一句話回應同行
5. Rodriguez PJ, et al. *JAMA Intern Med* 2024;184:1056 ＋ NHS England／NICE TA1026／CMS Bridge — 「真實世界三分之一未達 5%」與「資源真的要分批」

備選：Ard 2025、Shah 2026 JGIM

### 3.7 建議講稿（3–4 句）

「這一頁我要強調的不是 AI 讓藥更有效——臨床試驗裡仍有約一成、真實世界約三分之一的人一年減不到 5%，而英國 NHS 要分 12 年才能把 tirzepatide 開放給所有符合資格的人、台灣健保則完全不給付減重適應症，藥物資源確實有限。目前最有力的證據是 Mayo 團隊在 *Cell Metabolism* 2025 用機器學習基因風險分數區分 liraglutide 反應者（−6.4% 對 −3.3%），以及 23andMe 在 *Nature* 2026 找到 GLP1R 的功能變異；但我必須誠實說，這些工具外部驗證的 AUC 只有 0.69 到 0.75、基因只解釋一小部分變異、Mayo 自己的隨機試驗 12 週兩組只差 1 個百分點，而且相關等位基因在東亞族群的頻率只有歐洲的四成。所以比較精確的說法是：AI 可能幫我們更早知道誰該換藥、誰需要多一點支持，而不是拿來決定誰不配用藥——真正配置資源時，仍應以臨床需求與公平為先。」

### 3.8 查不到（不猜）

DDW 2024 semaglutide Hungry Gut 全文；ADA 2025 tirzepatide/semaglutide GRS 摘要數字；NCT03374956 期刊發表；健保署減重適應症不給付的正式新聞稿；週纖達台灣上市日、猛健樂增列肥胖適應症日期（僅次級來源）；*Nature* 2026 引用的「semaglutide 32.2% 減 <5% 或增重」原始出處；SURMOUNT-5 分級反應比例。
