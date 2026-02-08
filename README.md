# 📈 my_stock: 個人化股市數據下載器

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat-square&logo=python&logoColor=white)
![Data](https://img.shields.io/badge/Data-JSON-orange?style=flat-square)
![Finance](https://img.shields.io/badge/Focus-Stock_Market-gold?style=flat-square)

這是一個輕量級的股市數據抓取與靜態視覺化工具，專為需要長期追蹤特定標的的投資者設計。

## 🌟 主要特色
- **跨市場支援**：同步追蹤台股 (TW) 與美股 (US) 熱門標的。
- **數據持久化**：自動將行情轉為結構化 JSON 檔案，利於後續數據清洗與分析。
- **極簡管理**：只需編輯 `watchlist.txt` 即可增減監控對象。
- **快速概覽**：內建 `index.html` 可快速檢視最新的市場數據。

## 📂 專案組成
```text
.
├── my_downloader.py    # Python 抓取核心
├── watchlist.txt       # 關注名單 (如: 2330.TW, NVDA)
├── my_stock_data/      # JSON 數據存儲庫
└── index.html          # 數據展示頁面
```

## 🛠️ 執行說明
確保已安裝 `yfinance` 等必要庫後執行：
```bash
python my_downloader.py
```

---
*數據驅動，冷靜佈局。*