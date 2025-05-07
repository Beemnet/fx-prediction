import yfinance as yf

# Yahoo ticker for USD to EUR is "EURUSD=X"
data = yf.download("EURUSD=X", period="5d", interval="1m", auto_adjust=True) 
# Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 4h, 1d, 5d, 1wk, 1mo, 3mo]
print(data.tail())
