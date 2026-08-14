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
- [ ] 階段四：HTML 離線簡報製作（`html-slide-builder` skill，`slides/spec.yaml` 已完成並通過驗證；**卡在 BG 底圖視覺風格**，見 handoff.md）
- [ ] 階段五：PPTX 版本製作（存 OneDrive，不進 git）
- [ ] 階段六：臨床數據套用四條鐵律二次核對（若有使用門診數據）

## 待確認事項（不擋流程，先記錄）
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
├── reference/
│   ├── material-inventory.md          舊簡報＋自製專案素材盤點（含減重評估表單／醫師輸入工具位置）
│   ├── ai-privacy-security-notes.md   AI醫療隱私個資講義筆記
│   └── citation-verification.md       2026新素材數字查證報告
├── content/
│   └── outline-50slides.md            50張投影片大綱 v2.1
└── slides/
    ├── spec.yaml                      HTML簡報規格（html-slide-builder skill 格式，已驗證）
    └── images/                        AI生圖草稿（4版golden sample皆未過關，未進git，見handoff.md）

最終成品（摘要 DOCX、簡報 PPTX）存放於
D:\潘湘如\演講\2026演講\肥胖醫學會南區研討會\，不進本 repo（見工作約定）
```

## 同步層級（本專案初始化至第 2 層級）

| 層級 | 平台 | 位置 | 讀取時機 |
|------|------|------|---------|
| L1 | 本地（`C:\projects\obesity-society-ai-talk\`） | `agents.md`＋`handoff.md` | 每個 session |
| L2 | GitHub（**跨電腦同步唯一管道**） | philia81301-commits/obesity-society-ai-talk（公開） | 指定時 |
| L3 | Obsidian | 未啟用（這台電腦沒有 Obsidian MCP，之後可在有 Obsidian 的電腦說「補建第三層級」） | 有需要時 |

## 工作約定
- 任何 Agent、任何電腦：**開工先讀 `handoff.md`，收工必更新 `handoff.md`**
- 修改共用檔案前先讀最新內容，避免覆蓋其他 Agent 的變更
- 所有回應與文件使用繁體中文
- 修改前先確認計畫，優先保留原有資料結構
- **repo 為公開**：門診數據一律去識別化、聚合呈現，套用臨床資料鐵律（性別編碼交叉驗證、n<10 不當亮點、藥物欄位先掃 distinct 值、個案限近一年仍回診者）；原始 `.xlsx`／`.csv` 等資料檔一律不進 git（見 `.gitignore`）
- PPTX／Word 等最終成品存放於 `D:\潘湘如\演講\2026演講\`（OneDrive 同步範圍），不進本 repo；本 repo 只放 HTML 原始碼與文件
