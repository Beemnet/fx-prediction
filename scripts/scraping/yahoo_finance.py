import yfinance as yf

# Yahoo ticker for USD to EUR is "EURUSD=X"
data = yf.download("EURUSD=X", period="5d", interval="1h")
print(data.tail())

