# 肥胖醫學會 AI 主題演講（專案藍圖）

> 本檔為跨 Agent 通用的專案藍圖（AGENTS.md 開放標準）。任何 Agent 的每個 session 都應先讀本檔＋`handoff.md`。

## 專案簡介
為台灣肥胖醫學會 2026 南區學術研討會製作一場 50 張投影片、40 分鐘的演講，講題「人工智慧在肥胖治療運用的新發展」。**架構為 v2（專業角度）**：以「發展脈絡（過去→現在）＋應用分類（診斷／管理／研究）」的學術回顧為主軸，講者自己已產出的 AI 專案（`agent-roadshow`、`osteoporosis-clinic`、`sarcopenia-clinic`）改列為第二段「現況實務」的案例佐證（機構視角，非個人敘事），最後一段是 AI 資訊安全與個資保護。最終同時產出 PPTX（供大會繳交存查，成品存 OneDrive／演講資料夾，不進 git）與離線可播的單一 HTML（現場播放，本 repo 管理原始碼）。

## 關鍵時程
- **演講日期：2026-09-20**（台灣肥胖醫學會 2026 南區學術研討會）
- **講題：人工智慧在肥胖治療運用的新發展**
- 講者：潘湘如 醫師｜高雄榮民總醫院家庭醫學部
- 格式：50 張投影片，40 分鐘（原假設 45-60 分鐘工作坊型，2026-08-14 使用者更新為此格式）
- 投稿截止日：未知，向大會確認後補上

## 目標與路線圖
- [x] 階段一：RDQ 需求訪談確認、專案初始化
- [x] 階段二：整理演講參考資料（見 `reference/material-inventory.md`、`reference/ai-privacy-security-notes.md`）
- [x] 階段三：內容大綱（`content/outline-50slides.md`，v2.1，50張，減重生態系為主線／其餘門診工具為輔線）＋ 摘要 DOCX 已產出
- [x] 階段四：HTML 離線簡報製作 —— 50 頁骨架完成、視覺系統定案（板塊識別色＋SVG 圖標＋資料視覺化）、
      P19／P21／P24 手繪底圖定案、離線化完成並實測。
      2026-08-15 補：**P1 封面底圖與立體標題定案**、P4 卡片放大、**P9 改以國際指引收錄現況取代無出處數字**、
      **P20／P25／P27／P30 四張工具截圖已嵌入**。**剩餘內容補件見 handoff.md**
- [x] 階段五：PPTX 版本製作（存 OneDrive，不進 git）——2026-08-15 產出 v1，50 頁 16:9、25 MB。
      作法為 `slides/build_pptx.py`：Playwright 以 1280×720、2 倍解析度逐頁截圖，
      python-pptx 滿版貼圖並把每頁文字寫進備忘稿（保留可搜尋性）。
      **內容有異動就重跑一次**，成品覆蓋同一資料夾。
- [x] 階段六：臨床數據套用四條鐵律二次核對 —— **P25 性別編碼交叉驗證經使用者於 2026-08-15 決定略過**，
      本階段結案（其餘三條鐵律：n<10 未當亮點、藥物欄位未做分組統計、展示個案皆為現行工具截圖，均無適用問題）
- [ ] 階段七：上台前定稿（2026-08-15 新增）——**2026-08-16 完成四項**：
      PPTX 右下角頁碼（`build_pptx.py` 不再隱藏 `.slide-number`）、P9 政策段改寫、
      P22 改為整頁資訊呈現（滑桿移除）、P40 補入責任歸屬與醫療廣告界線。
      **剩餘三項皆只有使用者能推進**：補門診實地照片、P23 敏感議題判定範圍（需醫院電腦 X108521）、
      建 Firebase 專案並填 `slides/live-config.js`

## ⚠️ 2026-08-16 重要事實修正（P9）

P9 原本斷言「**AI 至今未寫進任何一條肥胖治療建議條文**」，**此說法不成立**。
使用者提供的 `成人肥胖指引 2025〈科技與虛擬醫療在體重管理的運用〉`（**講者本人執筆**）
含 6 條 GRADE 建議，其中兩條直接針對 AI：AI 聊天機器人（2C）、臨床決策輔助系統 CDSS（2C），
另有醫療科技介入整體列 1A。骨鬆指引對照句（「肥胖領域還沒輪到」）也連帶失效。

P9 已改寫為**證據等級落差**論述（1A → 2C），並亮出講者的作者身分。
⚠️ **日後任何「AI 未被指引收錄」的表述都要先核對這份指引**，不要再犯。
來源檔：`C:\Users\phili\OneDrive\文件\obesity\docx\[終版]_成人肥胖指引2025_...docx`（42 篇附 DOI 文獻）。

## 待確認事項（不擋流程，先記錄）
- [x] ~~P22 改成什麼形式~~ 2026-08-16 定案：整頁靜態機制對照，滑桿移除
- [x] ~~簡報視覺風格~~ 版面／字型／色彩已定案（見下），**但BG底圖的具體圖案風格仍未定案**，見 handoff.md
- [x] ~~大綱 P28-30／P32-34「減重門診月報自動化＋遊戲」案例素材~~ 已定位並納入大綱（2026-08-14）
- [x] ~~2026新素材數字查證~~ 已完成，見 `reference/citation-verification.md`，結果已回填大綱
- [ ] 大綱裡標記「⚠️需查證」的 2026 新素材數字，製作前需回頭核實原始文獻

## HTML簡報設計定案（2026-08-14）
- 版面／字型／色彩：學術沉穩風，白底墨綠（`#1B4332`），標題用Noto Serif TC，內文Noto Sans TC，詳見 `slides/spec.yaml` 的 `design_system`
- 內容結構：`slides/spec.yaml`（50張，已過 `validate_spec.py`）——Ⅱ現況實務段以減重門診工具為主線（評估表單雙軌蒐集→AI管理系統RAG→月度分析自動化＋遊戲），骨鬆／肌少症／HP-clinic／pneumonia-clinic為輔線
- BG／ICON分布：BG 15頁（每個板塊開篇＋Ⅱ段每個子案例開篇）、ICON 5頁，皆已超出skill建議值但為使用者明確要求
- **BG底圖風格尚未定案**：已試4版皆被否決，詳見 handoff.md「下一步」

## 資料夾結構
```
obesity-society-ai-talk/
├── agents.md
├── handoff.md
├── .gitignore
├── rdq/
│   └── RDQ-spec-obesity-society-ai-talk-20260814.md   需求規格卡（revisions:4）
├── index.html                        ★觀眾填答頁（手機版，GitHub Pages 發布，P2 的 QR 指向這裡）
├── reference/
│   ├── material-inventory.md          舊簡報＋自製專案素材盤點（含減重評估表單／醫師輸入工具位置）
│   ├── ai-privacy-security-notes.md   AI醫療隱私個資講義筆記
│   ├── citation-verification.md       2026新素材數字查證報告
│   ├── guideline-ai-scan-20260815.md  ★ADA 2026與國際肥胖學會「AI收錄現況」掃描（P9 的出處依據）
│   ├── osteoporosis-guideline-scan-20260815.md  ★骨鬆工具判定邏輯的指引溯源（P30 標註依據）
│   ├── firebase-setup.md              ★現場互動的建置步驟＋Firestore 安全性規則全文
│   ├── north-talk-20260524-digest.md  ★北區場（2026-05-24）56 頁逐頁摘要＋數字可信度分級
│   │                                    ＋附錄：同資料夾第二份簡報（TFDA 法規／2026-05 生成式 AI 指引）
│   └── legal-citations-20260816.md    ★醫師法／醫療法條號查證（P40 引註依據，含查不到的部分）
├── content/
│   └── outline-50slides.md            50張投影片大綱 v2.1
└── slides/
    ├── index.html                     ★簡報本體（50頁，離線可播）
    ├── spec.yaml                      HTML簡報規格（html-slide-builder skill 格式，已驗證）
    ├── live-config.js                 ★現場互動設定（Firebase config 待填，未填會自動降級）
    ├── build_fonts.py                 中文字型子集化腳本（改內文後需重跑，見下方離線化）
    ├── build_qr.py                    產生 P2 的作答 QR（網址改了要重跑）
    ├── build_pptx.py                  ★HTML→PPTX 轉檔（階段五，內容異動就重跑）
    ├── vendor/                        reveal.js 5.1.0 本地副本（reset.css／reveal.css／reveal.js）
    ├── fonts/                         Noto Sans/Serif TC 子集 woff2（*-VF.ttf 來源檔不進 git）
    └── images/                        P1 封面底圖、P19／P21／P24 手繪底圖（已定案採用）
                                       ＋ p20/p25/p27/p30 四張工具操作截圖
                                       ⚠️ 新圖不可命名 cover_*.png（.gitignore 擋掉該樣式）
                                       generated/ 為 draw 技能原始輸出，不進 git

最終成品（摘要 DOCX、簡報 PPTX）不進本 repo（見工作約定）。
⚠️ 路徑因電腦而異：**家用 DESKTOP-LVSV9Q5 沒有 D 槽**，
2026-08-15 起改存 C:\Users\phili\OneDrive\文件\演講\2026演講\肥胖醫學會南區研討會\
（同一個 OneDrive 同步範圍，醫院端 D:\潘湘如\演講\2026演講\ 應為同一份雲端資料夾的不同掛載點，
到醫院時請確認，若不是同一份要手動搬過去）
```

## 離線化（2026-08-14 完成，現場播放的命脈）

演講廳網路不可靠，簡報**所有資產一律本地**，`index.html` 內**不得出現任何 CDN 連結**。
已實測：載入時零外部請求，字型與底圖皆正常。

| 資產 | 位置 | 備註 |
|------|------|------|
| reveal.js 5.1.0 | `slides/vendor/` | reset.css／reveal.css／reveal.js |
| 中文字型 | `slides/fonts/*-subset.woff2` | variable font，單檔涵蓋 100–900 全字重 |
| 底圖 | `slides/images/*.png` | 3 張，共約 6.7 MB |

**⚠️ 改動 `index.html` 內文後，必須重跑字型子集化**，否則新字會變豆腐：

```bash
cd slides && python build_fonts.py
```

腳本會自動比對缺字並警告；來源 VF 檔（27MB，不進 git）缺少時會自動下載。
子集包含「簡報實際用字 ＋ Big5 常用字 5400 字」作安全邊際，小幅改字通常不會缺。

> 踩過的坑：Google Fonts CDN 的 `chinese-traditional` 分割子集**缺全形標點（，／：）與羅馬數字（Ⅰ Ⅱ Ⅲ）**，
> 直接拿來用會滿頁豆腐字。因此改為從完整 variable font 自行切子集。

## 同步層級（本專案初始化至第 2 層級）

| 層級 | 平台 | 位置 | 讀取時機 |
|------|------|------|---------|
| L1 | 本地（`C:\projects\obesity-society-ai-talk\`） | `agents.md`＋`handoff.md` | 每個 session |
| L2 | GitHub（**跨電腦同步唯一管道**） | philia81301-commits/obesity-society-ai-talk（公開） | 指定時 |
| L3 | Obsidian | `2ndBrain/obesity-society-ai-talk/專案工作流程.md`（2026-08-15 補建） | 需要完整背景脈絡時 |

## 工作約定
- 任何 Agent、任何電腦：**開工先讀 `handoff.md`，收工必更新 `handoff.md`**
- 修改共用檔案前先讀最新內容，避免覆蓋其他 Agent 的變更
- 所有回應與文件使用繁體中文
- 修改前先確認計畫，優先保留原有資料結構
- **repo 為公開**：門診數據一律去識別化、聚合呈現，套用臨床資料鐵律（性別編碼交叉驗證、n<10 不當亮點、藥物欄位先掃 distinct 值、個案限近一年仍回診者）；原始 `.xlsx`／`.csv` 等資料檔一律不進 git（見 `.gitignore`）
- PPTX／Word 等最終成品存放於 `D:\潘湘如\演講\2026演講\`（OneDrive 同步範圍），不進本 repo；本 repo 只放 HTML 原始碼與文件
