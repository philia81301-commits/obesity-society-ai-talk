---
rdq_version: 1
task: 肥胖醫學會 AI 主題演講製作
domain: workshop
date: 2026-08-14
status: confirmed
telemetry:
  mode: full
  rounds: 1
  questions: 4
  q4_adopted: 2
  revisions: 1
downstream: self
---

# RDQ 需求規格：肥胖醫學會 AI 主題演講製作

## 一句話任務
為肥胖醫學會製作一場 45-60 分鐘工作坊型 AI 主題演講：開場先講肥胖醫學 AI 研究趨勢，實戰段落展示講者自己已產出的減重／衛教 AI 專案，同時產出 PPTX＋離線 HTML。

## ✅ 已確認
- 內容順序：開場先以「肥胖醫學 AI 研究趨勢」（②）鋪陳，再進入實戰應用（①③）（使用者修改）
- 研究趨勢段落參考講者既有的 AI 主題演講素材：`D:\潘湘如\演講\AI\2025\`（AI協助體重控制）、`AI\2026\`（AI×GLP-1藥物效能與患者成效、GLP1_AI_SideEffects_Analysis、減重門診AI管理、Agentic AI、discussion about AI、AI_noon_WW）等既有檔案（使用者修改）
- 實戰／案例分享改用講者自己已產出的真實專案，不用假設性範例：`C:\projects\agent-roadshow`（AI Agent 醫療職場入門）、`C:\projects\osteoporosis-clinic`、`C:\projects\sarcopenia-clinic`（篩檢工具網頁）等（使用者修改）
- 聽眾：肥胖醫學會會員為主（Ⅲ）
- 時長：45-60 分鐘工作坊型（Ⅲ）
- 交付格式：PPTX ＋ HTML 兩者都要（Ⅲ）
- 若秀門診真實數據，先套用臨床資料鐵律（性別編碼交叉驗證、n<10 不當亮點、藥物欄位先掃 distinct 值、個案限近一年仍回診者）（Ⅳ 採納）
- HTML 版做成離線可播版本（Ⅳ 採納）
- 執行方式：分段進行，先做「整理演講資料」這一階段，不要一次做到底（使用者於確認時追加）

## ❓ 假設（未確認，已採預設值，隨時可推翻）
- 演講日期／投稿截止日 → 未知，需向大會索取
- 確切聽眾人數 → 假設約 50-150 人
- 現場網路／設備 → 未知，已用離線 HTML 因應
- 是否錄影或事後公開播出 → 未知（見排除項）
- ①③實戰段落具體要放哪幾個專案、放多少張投影片 → 尚未細談，先假設 agent-roadshow ＋ 兩個篩檢網站都放，實際製作時再依篇幅取捨

## ➕ 已採納（象限Ⅳ）
- 秀門診數據前先套臨床鐵律二次核對
- 離線可播的 HTML 備援版

## ❌ 排除項（明確不做）
- 不主動確認錄影／公開範圍與著作權出處頁
- 不安排現場 AI 工具 live demo 環節

## 📋 一段式需求規格
為肥胖醫學會製作一場 45-60 分鐘工作坊型演講，主題是 AI 在肥胖醫學／減重門診的應用。內容順序先以「肥胖醫學 AI 研究趨勢」開場（參考講者既有的 `D:\潘湘如\演講\AI\2025\` 與 `AI\2026\` 資料夾內既有簡報，如 AI協助體重控制、AI×GLP-1藥物效能與患者成效、減重門診AI管理、Agentic AI 等），再進入實戰應用段落，用講者自己已經做出來、實際在用的 AI 專案當真實案例——`C:\projects\agent-roadshow`（AI Agent 醫療職場入門教材）、`C:\projects\osteoporosis-clinic`、`C:\projects\sarcopenia-clinic`（骨鬆／肌少症篩檢網頁工具）——取代泛用範例，呼應「醫師如何用 AI 工具提效」與「減重門診臨床應用」兩個主軸。聽眾以肥胖醫學會會員為主，假設規模約 50-150 人。最終同時產出 PPTX（供大會繳交存查，存放於 `D:\潘湘如\演講\2026演講\`，不進 git）與單一離線 HTML（現場播放，斷網也能跑，素材需內嵌單檔，原始碼放本 repo）。若內容展示門診真實數據，需先依講者的臨床資料鐵律做性別編碼交叉驗證、排除 n<10 亮點、藥物欄位先列 distinct 值、個案限近一年仍回診者，才能進入製作。專案建立在 `C:\projects\obesity-society-ai-talk`（GitHub 公開 repo）。執行採分段進行，先完成「整理演講參考資料」這一階段並給使用者確認，才進入內容大綱與製作。演講日期、確切人數、投稿截止日、是否錄影公開等細節目前未知。

## ✔ 驗收條件
- [ ] `C:\projects\obesity-society-ai-talk` 建立完成，含 PPTX 與 HTML 兩份成品
- [ ] 開場研究趨勢段落有引用／改編自 `D:\潘湘如\演講\AI\` 既有素材
- [ ] 實戰段落至少展示 agent-roadshow、osteoporosis-clinic、sarcopenia-clinic 其中的真實成果畫面或數據
- [ ] 若含門診數據，四條臨床鐵律皆已套用
- [ ] HTML 版離線也能正常播放（斷網測試過）
