import yfinance as yf
import os

# Directory to save the CSV files
output_dir = '../../data/raw/yahoo_exchange'
os.makedirs(output_dir, exist_ok=True)

# Mapping of intervals to maximum available periods
interval_period_map = {
    '1m': '7d',       # Actually 8d, but 7d is safe
    '2m': '60d',
    '5m': '60d',
    '30m': '60d',
    '60m': '60d',
    '1d': '3mo'
}

ticker = "EURUSD=X"

for interval, period in interval_period_map.items():
    print(f"Downloading {ticker} data: interval={interval}, period={period}")
    try:
        data = yf.download(
            tickers=ticker,
            period=period,
            interval=interval,
            auto_adjust=True,
            progress=False
        )
        if not data.empty:
            filename = f"yahoo_exchange_{period}_{interval}.csv"
            file_path = os.path.join(output_dir, filename)
            data.to_csv(file_path)
            print(f"Saved: {file_path}")
        else:
            print(f"No data returned for interval={interval}, period={period}")
    except Exception as e:
        print(f"Error downloading {interval} data: {e}")
