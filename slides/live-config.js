/* ============================================================
   現場互動設定檔（簡報端與觀眾填答頁共用）
   ------------------------------------------------------------
   ⚠️ 這是整套互動功能唯一需要手動填的地方。
   填寫步驟見 reference/firebase-setup.md（含 Firestore 安全性規則全文）。
   未填之前，簡報 P2／P38 會自動顯示「互動未啟用」的靜態說明，
   不會出錯、不影響其餘 48 頁的離線播放。
   ============================================================ */
window.TALK_LIVE = {

  /* ↓↓↓ Firebase Console → 專案設定 → 一般 → 你的應用程式 → SDK 設定與配置 → 「設定」
         把整個 firebaseConfig 物件的六個值貼過來取代 PASTE_* */
  firebaseConfig: {
    apiKey:            "AIzaSyBXXCQ5x0iWicUfe47U5LTgz3_83MrDNB4",
    authDomain:        "obesity-ai-firebase.firebaseapp.com",
    projectId:         "obesity-ai-firebase",
    storageBucket:     "obesity-ai-firebase.firebasestorage.app",
    messagingSenderId: "343364935435",
    appId:             "1:343364935435:web:ce3e80555052f4f3c1cc0e"
  },

  /* Firestore 集合名稱。用本場專屬名稱，避免跨場次資料污染。
     改名的話 Firestore 安全性規則裡的路徑也要一起改。 */
  wordcloudCollection: 'obesity_ai_talk_wordcloud',
  pollCollection:      'obesity_ai_talk_poll',

  /* P38 投票選項。id 只能是 a/b/c/d（安全性規則有白名單，要增減選項需同步改規則）。 */
  pollOptions: [
    { id: 'a', label: '資料蒐集自動化' },
    { id: 'b', label: 'AI 病人溝通' },
    { id: 'c', label: 'AI 資料分析' },
    { id: 'd', label: '自動化篩檢合適減重藥物' }
  ],

  /* 觀眾填答頁網址（QR code 指向這裡）。
     改網址後要重跑：python build_qr.py */
  audienceUrl: 'https://philia81301-commits.github.io/obesity-society-ai-talk/',

  /* 每人文字雲最多可送出幾次（擋洗版，存在瀏覽器 localStorage，非強制） */
  wordcloudMaxPerDevice: 3
};

/* 判斷是否已完成設定 —— 簡報端與觀眾端都用這個函式決定要不要連線。 */
window.TALK_LIVE.isConfigured = function () {
  var k = window.TALK_LIVE.firebaseConfig.apiKey;
  return typeof k === 'string' && k.indexOf('PASTE_') !== 0 && k.length > 10;
};
