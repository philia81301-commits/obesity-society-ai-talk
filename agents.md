# 肥胖醫學會 AI 主題演講（專案藍圖）

> 本檔為跨 Agent 通用的專案藍圖（AGENTS.md 開放標準）。任何 Agent 的每個 session 都應先讀本檔＋`handoff.md`。

## 專案簡介
為肥胖醫學會會員製作一場 45-60 分鐘工作坊型演講，主題是「AI 在肥胖醫學／減重門診的應用」。開場先講肥胖醫學 AI 研究趨勢，實戰段落展示講者自己已產出的 AI 專案（`agent-roadshow`、`osteoporosis-clinic`、`sarcopenia-clinic`）。最終同時產出 PPTX（供大會繳交存查，成品存 OneDrive／演講資料夾，不進 git）與離線可播的單一 HTML（現場播放，本 repo 管理原始碼）。

## 關鍵時程
- **演講日期：2026-09-20**（台灣肥胖醫學會 2026 南區學術研討會）
- **講題：人工智慧在肥胖治療運用的新發展**
- 講者：潘湘如 醫師｜高雄榮民總醫院家庭醫學部
- 格式：50 張投影片，40 分鐘（原假設 45-60 分鐘工作坊型，2026-08-14 使用者更新為此格式）
- 投稿截止日：未知，向大會確認後補上

## 目標與路線圖
- [x] 階段一：RDQ 需求訪談確認、專案初始化
- [x] 階段二：整理演講參考資料（見 `reference/material-inventory.md`、`reference/ai-privacy-security-notes.md`）
- [x] 階段三：內容大綱（`content/outline-50slides.md`，50張三板塊比例配置）＋ 摘要 DOCX 已產出
- [ ] 階段四：HTML 離線簡報製作（風格待使用者確認）
- [ ] 階段五：PPTX 版本製作（存 OneDrive，不進 git）
- [ ] 階段六：臨床數據套用四條鐵律二次核對（若有使用門診數據）

## 待確認事項（不擋流程，先記錄）
- [ ] 簡報視覺風格尚未確認
- [ ] 大綱 P28-30「減重門診月報自動化＋遊戲」案例素材尚未定位
- [ ] 大綱裡標記「⚠️需查證」的 2026 新素材數字，製作前需回頭核實原始文獻

## 資料夾結構
<!-- 初始化時尚無內容檔案，之後新增請更新本區塊 -->
```
obesity-society-ai-talk/
├── agents.md
├── handoff.md
├── .gitignore
├── rdq/
│   └── RDQ-spec-obesity-society-ai-talk-20260814.md
├── reference/
│   ├── material-inventory.md          舊簡報＋自製專案素材盤點
│   └── ai-privacy-security-notes.md   AI醫療隱私個資講義筆記
└── content/
    └── outline-50slides.md            50張投影片大綱

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
