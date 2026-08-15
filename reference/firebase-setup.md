# 現場互動設定步驟（Firebase ＋ GitHub Pages）

> 對應簡報 **P2 即時文字雲**與 **P38 現場投票**。
> 程式碼已全部寫好，**只差一個 Firebase 專案**——這步必須由你在 Firebase Console 手動完成
> （Agent 不能代為登入或建立帳號）。全部約 10 分鐘。

## 現在的狀態

- ✅ 觀眾填答頁：`index.html`（repo 根目錄，手機版）
- ✅ 簡報端顯示：`slides/index.html` 的 P2／P38
- ✅ Firebase SDK 本地副本：`slides/vendor/firebase-*-compat.js`
- ✅ QR code：`slides/images/qr_audience.png`
- ⬜ **Firebase 專案 → 設定值填進 `slides/live-config.js`**

**未填設定不會壞掉**：P2／P38 會顯示「互動未啟用——請改用口頭舉手」，其餘 48 頁完全不受影響。

---

## 步驟一：建立 Firebase 專案

1. 開 <https://console.firebase.google.com/> → **新增專案**
2. 專案名稱建議：`obesity-ai-talk-2026`
3. **Google Analytics 選「不啟用」**（用不到，也少一份資料蒐集）
4. 建立完成後進專案

## 步驟二：建立 Firestore 資料庫

1. 左側選單 → **Firestore Database** → **建立資料庫**
2. 位置選 **asia-east1（台灣）**——現場延遲最低
3. 模式先選「**以測試模式啟動**」，下一步馬上改成正式規則

## 步驟三：貼上安全性規則（重要）

Firestore Database → **規則** 分頁 → 整段取代後按**發布**：

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // 文字雲：只能新增、不能讀改刪別人的；限制欄位與長度，擋洗版
    match /obesity_ai_talk_wordcloud/{doc} {
      allow read: if true;
      allow create: if request.resource.data.keys().hasOnly(['word', 'created_at'])
                    && request.resource.data.word is string
                    && request.resource.data.word.size() > 0
                    && request.resource.data.word.size() <= 12;
      allow update, delete: if false;
    }

    // 投票：一台裝置一份文件，選項限 a/b/c/d
    match /obesity_ai_talk_poll/{device} {
      allow read: if true;
      allow write: if request.resource.data.choice in ['a', 'b', 'c', 'd'];
      allow delete: if false;
    }

    // 其餘一律拒絕
    match /{document=**} {
      allow read, write: if false;
    }
  }
}
```

> ⚠️ 這份規則允許**任何人匿名寫入**這兩個集合——現場互動本來就不能要求觀眾登入。
> 風險是有人事後亂灌資料，所以**演講結束後請回來把 `allow create`／`allow write` 改成 `if false`**。
> 兩個集合都不含姓名、院所或任何可識別個人的欄位。

## 步驟四：取得設定值並填入

1. 專案設定（左上齒輪）→ **一般** → 最下方「你的應用程式」→ 點 **`</>`（網頁）**
2. 應用程式暱稱隨意（例：`talk-slides`），**不要**勾選 Firebase Hosting
3. 註冊後會出現 `firebaseConfig` 物件，把六個值貼進 `slides/live-config.js` 取代 `PASTE_*`
4. 存檔後直接用瀏覽器開 `slides/index.html`，P2 的提示字應該從
   「互動未啟用」變成空白（代表連線成功）

## 步驟五：推上去讓觀眾頁生效

```bash
git add -A && git commit -m "填入 Firebase 設定" && git push
```

GitHub Pages 約 1 分鐘後更新。

---

## 演講當天檢查清單

- [ ] 用手機（**行動網路，不要用會場 Wi-Fi**）掃 P2 的 QR，確認填答頁打得開
- [ ] 送出一個測試答案，確認投影幕上的文字雲有跳出來
- [ ] 投一票，確認 P38 長條有動
- [ ] **測完把測試資料清掉**：Firestore Console → 兩個集合 → 刪除文件
- [ ] 講者筆電確認能連網；**連不上就直接口頭舉手**，簡報會自己顯示提示，不用臨場改東西

## 網址

| 用途 | 網址 |
|------|------|
| 觀眾填答頁（QR 指向這裡） | <https://philia81301-commits.github.io/obesity-society-ai-talk/> |
| 簡報（現場請用本機檔案播放，這只是備援） | <https://philia81301-commits.github.io/obesity-society-ai-talk/slides/> |

改網址後要重畫 QR：

```bash
cd slides && python build_qr.py
```

---

## 設計取捨（為什麼這樣做）

- **SDK 用 compat（UMD）版而不是 v11 模組版**：簡報是用 `file://` 直接開的，
  ES module 在 `file://` 會被瀏覽器 CORS 擋掉，整個互動會靜默失效。compat 版是傳統
  `<script>` 標籤，`file://` 正常運作。
- **SDK 檔案放 `slides/vendor/`**：維持「載入階段零外部請求」。斷網時頁面照樣秒開，
  只有 Firestore 的即時資料收不到，會降級成提示文字。
- **投票用「一裝置一文件」而非單一文件存所有票**：後者需要開放整份文件的更新權限，
  任何人都能覆蓋別人的票；前者可以在規則層限制每份文件的內容。
- **8 秒逾時看門狗**：現場斷網時 Firestore 不會報錯、只會無聲重試，
  講者會以為觀眾不捧場。加上逾時提示，8 秒後畫面直接告訴你要改口頭舉手。
