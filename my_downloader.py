import yfinance as yf
import pandas as pd
import os
import json
from datetime import datetime

# 1. 設定
OUTPUT_DIR = "my_stock_data"
WATCHLIST_FILE = "watchlist.txt"
METADATA_FILE = "metadata.json"

# 確保資料夾存在
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# 2. 讀取觀察名單
stock_list = []
if os.path.exists(WATCHLIST_FILE):
    with open(WATCHLIST_FILE, "r") as f:
        stock_list = [line.strip() for line in f if line.strip()]
else:
    stock_list = ["2330.TW"]

print(f"📋 準備下載 {len(stock_list)} 檔股票的完整歷史數據...")

# 用來記錄成功的股票
success_list = []

# 3. 開始下載
for symbol in stock_list:
    print(f"⬇️ 正在下載: {symbol} ...")
    try:
        df = yf.download(symbol, period="max", progress=False)
        
        if df.empty:
            print(f"⚠️ {symbol} 下載為空，跳過。")
            continue

        if isinstance(df.columns, pd.MultiIndex):
             try:
                 df = df.xs(symbol, axis=1, level=1)
             except:
                 pass
        
        required_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
        available_cols = [c for c in required_cols if c in df.columns]
        df = df[available_cols]
        
        df.index = df.index.tz_localize(None)
        json_str = df.to_json(orient="index", date_format="iso", double_precision=2)
        
        file_path = os.path.join(OUTPUT_DIR, f"{symbol}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(json_str)
            
        print(f"✅ 已儲存: {file_path}")
        success_list.append(symbol)

    except Exception as e:
        print(f"❌ {symbol} 發生錯誤: {e}")

# 4. 生成 Metadata (給網頁讀取用)
metadata = {
    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S (UTC)"),
    "stocks": success_list
}
with open(METADATA_FILE, "w", encoding="utf-8") as f:
    json.dump(metadata, f, ensure_ascii=False, indent=2)

print("\n🎉 全部任務完成，已更新 Metadata！")