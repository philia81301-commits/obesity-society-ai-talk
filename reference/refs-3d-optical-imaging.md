# 文獻卡：3D 光學體型掃描（3DO）與 NeRF／Gaussian Splatting——「新科技在肥胖醫學的應用」

> 建立：2026-10-20（office 這台）。來源：PubMed 檢索＋逐篇讀摘要（**尚未讀全文**）。
> 用途：12/13 台灣肥胖醫學會 AI 場（obesity-society-ai-talk P13.1–13.4）。
> 2026-10-20 使用者指示：**2019 年（含）以前的文獻太舊，不用**——已刪 T01 Ng 2019、T04 Wong 2019；之後指示 2020 的 T07 Tian 也換掉，改 T12／T13（編號保留不補位）。

## 一句話主軸

只靠「身體外形」（3D 光學掃描，甚至手機照片）就能估出接近 DXA 的體脂與瘦體組織。它不用輻射、可以重複做，**能追蹤減重過程中的體組成變化**。NeRF／Gaussian Splatting 是同一類「多張照片重建 3D」技術的下一代，目前醫學上主要用在視覺化，還沒有體組成的驗證研究。

## 技術層級（投影片可用的三層架構）

| 層級 | 設備 | 代表研究 |
|---|---|---|
| 1. 專用 3D 掃描機 | Fit3D ProScanner、Styku、SS20 等（站上轉盤或掃描間） | Shape Up! 系列（T02、T03、T05、T06） |
| 2. 手機 3D 掃描 | 手機 App 繞身拍攝產生 avatar | T08–T10 |
| 3. 手機 2D 照片 | 手機拍正面／側面照 | T12、T13 |
| （前沿）NeRF／3DGS | 多視角照片 → 照片級 3D | T11（法醫視覺化，非體組成） |

---

## 核心文獻（Shape Up! 系列：Hawaii Cancer Center Shepherd JA＋Pennington Heymsfield SB 團隊）

### T02 Wong 2021 Obesity——擺姿標準化後更準
- Wong MC, et al. *Obesity* 2021;29(11):1835-1847. PMID 34549543. doi:10.1002/oby.23256
- n = 472（分析數）。把掃描「數位重擺」成標準姿勢後再建模
- 脂肪量 R² = 0.91（男）/ 0.94（女）；去脂體重 0.95 / 0.92；內臟脂肪 0.77 / 0.79
- ✅ 2026-10-20 PMC 全文確認為 R²（PubMed 純文字摘要掉了上標）

### T03 Wong 2023 AJCN——**能追蹤介入期間的體組成變化**（和減重門診最相關）
- Wong MC, et al. *Am J Clin Nutr* 2023;117(4):802-813. PMID 36796647. doi:10.1016/j.ajcnut.2023.02.006
- 回溯分析 6 個介入研究，n = 133（女 45），追蹤平均 13 週（3–23 週）
- 6 個研究：女籃季前訓練、**減重手術**、低醣減重飲食（目標減 15%）、高齡阻力運動 16 週、限時進食 16:8、軍人睪固酮試驗——**沒有任何減重藥物研究**
- 3DO 變化量 vs DXA 變化量的一致性（R²）：
  - 女：脂肪量 0.86、去脂體重 0.73、四肢瘦體組織 0.70；RMSE 1.98 / 1.58 / 0.37 kg
  - 男：0.75、0.75、0.52；RMSE 2.31 / 1.77 / 0.52 kg
- 作者結論：靈敏度足以偵測介入期間的小幅變化，安全、可自行頻繁量測
- ✅ 2026-10-20 PMC 全文確認為 R²
- **投影片重點：減重藥物時代最在意「掉的是脂肪還是肌肉」，3DO 是不用輻射的追蹤選項**

### T05 Garber 2023 AJCN——低 BMI／飲食疾患
- Garber AK, et al. *Am J Clin Nutr* 2023;118(4):812-821. PMID 37598747. doi:10.1016/j.ajcnut.2023.08.004
- n = 95（低 BMI，部分為飲食疾患轉介）
- 與 DXA 一致性（Lin's CCC）：去脂體重 0.97、四肢瘦體組織 0.86、脂肪量 0.87
- DXA 判定的營養不良／肌少症個案，3DO 抓出 95%
- 可接 12/27 場身心章節（飲食疾患）

### T06 Leong 2024 Commun Med——從 3D 體型「生成」DXA 影像
- Leong LT, et al. *Commun Med* 2024;4(1):13. PMID 38287144. doi:10.1038/s43856-024-00434-w
- 深度學習從 3D 掃描生成假 DXA 影像，再用商用 DXA 軟體分析
- 全身脂肪量 R² 0.73、去脂體重 0.89；大腿區域 0.70–0.89
- 適合當「AI × 影像」的視覺亮點頁

## 從掃描機走向手機／照片

### T12 Majmudar 2022 npj Digit Med——手機 2D 照片估體脂率（取代 T07 Tian 2020）
- Majmudar MD, et al. *NPJ Digit Med* 2022;5(1):79. PMID 35768575. doi:10.1038/s41746-022-00628-3
- 一般手機相機拍 2D 照片，卷積神經網路估體脂率（visual body composition, VBC）；兩中心（MGH、PBRC）n = 134，21–76 歲，BMI 18.5–51.6
- 對照 DXA：平均絕對誤差 2.16 ± 1.54%；CCC 全體 0.96（女 0.93、男 0.94）；BMI 的 CCC 僅 0.45
- Bland-Altman 無顯著偏差（−0.42%），一致性界限 −5.5% 至 +4.7%；優於所有比較的 BIA 與 ADP
- ⚠️ **Amazon 員工主導（廠商研究）**，投影片已標註

### T13 Encarnação 2026 Clin Nutr ESPEN——獨立比較 3 款手機 App
- Encarnação IGA, et al. *Clin Nutr ESPEN* 2026;75:103391. PMID 42303133. doi:10.1016/j.clnesp.2026.103391
- n = 57 健康成人；MeThreeSixty、Bodygram（雙照片）、ZOZO Fit（12 張照片）
- 重測信度極佳（ICC 0.98–0.99）；但**三款都顯著低估體脂率**（偏差 −1.2% 至 −2.1%）
- 最好的 ZOZO Fit：RMSE 2.95%、CCC 0.90；**沒有一款落在 DXA ±2% 等效範圍內**，一致性界限都寬，App 之間不可互換
- 作者結論：目前不支持用於群體監測、臨床診斷或個人決策

### T08 Florez 2024 Br J Nutr——手機 3D 掃描＋美軍單點體脂公式
- Florez CM, et al. *Br J Nutr* 2024;132(9):1143-1151. PMID 39411840. doi:10.1017/S0007114524002216
- n = 96 名年輕成人，對照 DXA 與四分室模型
- 群體平均可接受，但**個人層級一致性界限寬**（體脂率 9.5–10.2%、脂肪量／去脂體重 6.8–7.8 kg），而且有比例性偏差
- **投影片但書頁用：群體可用，個人判讀要小心**

### T09 Minetto 2023 Sci Rep——手機 App 用於青少年足球員
- Minetto MA, et al. *Sci Rep* 2023;13:20734. PMID 38007571. doi:10.1038/s41598-023-48055-y
- n = 193（男 124／女 69），重複拍攝再現性好（%SEM < 10%）
- 但相對 DXA：體脂率高估（男 +3.7%、女 +4.6%），瘦體組織低估
- ⚠️ 共同作者含 App 廠商（Size Stream LLC）員工，有利益衝突要註明

### T10 Graybeal 2026 Mil Med——12 週訓練前後的追蹤效度
- Graybeal AJ, et al. *Mil Med* 2026. PMID 41934316. doi:10.1093/milmed/usag107
- 美國空軍 ROTC 學員，基線 n = 57、追蹤 n = 50
- 追蹤 12 週的體脂率**變化量**：手機 3DO 與近紅外光（NIRS）跟 DXA 最一致
- 附帶發現：BMI 達標者 57.9%，但用 DXA 體脂率判定只有 33.3% 達標（BMI 誤判）

## NeRF／Gaussian Splatting 的醫學現況

### T11 Thali 2026 Forensic Sci Med Pathol——3DGS 用於法醫全身記錄
- Thali M, Herr J, Gascho D. 2026. PMID 42700311. doi:10.1007/s12024-026-01353-z
- 多相機攝影測量做全身 360° 模型，另外用 3D Gaussian Splatting 做即時、高擬真的視覺化
- **作者明講：3DGS 目前是為視覺化最佳化，尺寸量測尚未經過驗證**
- 投影片用法：說明這項技術「看起來很真，但還不能拿來量」

### 補充（工程類，PubMed 有收但非臨床）
- Cao 2025 IEEE TVCG（PMID 40031791）：單一相機＋3DGS 即時全息病人影像，用於遠距復健，可在 HoloLens 2 上顯示——**與 VR／AR 最直接相關**
- 其餘 NeRF／3DGS 人體重建論文多為電腦視覺領域（虛擬人、服裝動態），不建議上投影片

## 背景綜述（可放參考文獻頁）
- Heymsfield SB, et al. Reference methods for measuring skeletal muscle mass. *J Cachexia Sarcopenia Muscle* 2026;17(1):e70184. PMID 41555669. doi:10.1002/jcsm.70184——把 3D 影像列在「需以 CT／MRI／DXA 校正的次級方法」
- DePrenger M, et al. Practical tools for evaluating body fat distribution. *Nutr Clin Pract* 2025;41(1):43-53. PMID 41207866. doi:10.1002/ncp.70065——含居家體型掃描 App
- （2017，偏舊，備查用）Bourgeois B, et al. *Eur J Clin Nutr* 2017;71(11):1329-1335. PMID 28876331. doi:10.1038/ejcn.2017.142——三種 3D 掃描機比較；周徑與體積相關性高，但重測變異大於參考方法

## 上投影片前待辦
1. ✅ T02、T03 已以 PMC 全文確認為 R²
2. ✅ 2026-10-20 決定：放 12/13 台灣肥胖醫學會 AI 場（沿用 9/20 obesity-society-ai-talk 51 頁版，插在 P13 之後 4 頁）
3. 若要示範 3DGS 實景，拍攝對象限空間與設備，不拍病人（隱私）
