# 📈 my_stock: 個人化股市數據下載器

這是一個輕量級的股市數據抓取與視覺化工具，專注於追蹤特定關注標的。

## 🌟 主要特色
- **自動化抓取**：使用 Python 腳本 `my_downloader.py` 定期抓取股市行情。
- **關注清單管理**：透過 `watchlist.txt` 輕鬆增減追蹤標的（支援台股與美股）。
- **數據緩存**：抓取的數據以 JSON 格式儲存於 `my_stock_data/`，方便離線分析。
- **靜態展示**：內建 `index.html` 用於展示分析結果。

## 📂 目錄結構
- `my_downloader.py`: 資料抓取核心。
- `watchlist.txt`: 股票清單。
- `my_stock_data/`: JSON 數據存儲路徑。

---
*精準追蹤，理性決策。*
