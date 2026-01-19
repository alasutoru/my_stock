import yfinance as yf
import pandas as pd
import os
import json
from datetime import datetime

# 1. 設定
OUTPUT_DIR = "my_stock_data"
WATCHLIST_FILE = "watchlist.txt"

# 確保資料夾存在
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# 2. 讀取觀察名單
stock_list = []
if os.path.exists(WATCHLIST_FILE):
    with open(WATCHLIST_FILE, "r") as f:
        stock_list = [line.strip() for line in f if line.strip()]
else:
    # 預設名單 (如果沒檔案的話)
    stock_list = ["2330.TW"] 

print(f"📋 準備下載 {len(stock_list)} 檔股票的完整歷史數據...")

# 3. 開始下載
for symbol in stock_list:
    print(f"⬇️ 正在下載: {symbol} ...")
    try:
        # 下載 Max 歷史數據
        df = yf.download(symbol, period="max", progress=False)
        
        if df.empty:
            print(f"⚠️ {symbol} 下載為空，跳過。")
            continue

        # 清洗數據：只保留 OHLCV
        # 注意：yfinance 新版回傳的 columns 可能是 MultiIndex，需要處理
        if isinstance(df.columns, pd.MultiIndex):
             # 嘗試扁平化或選取特定層級，這裡簡單處理：如果第一層是 Price，就丟掉
             # 通常 yfinance 格式是 (Price, Ticker) -> ('Open', '2330.TW')
             try:
                 df = df.xs(symbol, axis=1, level=1)
             except:
                 pass # 如果結構不如預期，維持原樣嘗試選取
        
        # 確保有這些欄位
        required_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
        available_cols = [c for c in required_cols if c in df.columns]
        df = df[available_cols]
        
        # 移除時區資訊 (避免 JSON 轉換錯誤)
        df.index = df.index.tz_localize(None)
        
        # 轉換為 JSON 格式 (以日期為 Key，或 Records 格式)
        # 這裡使用 'index' 格式： {"2024-01-01": {"Open": 500, ...}, ...}
        # 這種格式查詢特定日期最快
        json_str = df.to_json(orient="index", date_format="iso", double_precision=2)
        
        # 存檔
        file_path = os.path.join(OUTPUT_DIR, f"{symbol}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(json_str)
            
        print(f"✅ 已儲存: {file_path}")

    except Exception as e:
        print(f"❌ {symbol} 發生錯誤: {e}")

print("\n🎉 全部任務完成！")
