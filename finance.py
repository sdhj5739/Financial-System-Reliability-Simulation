import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

data = yf.download("AAPL", start="2020-01-01", end="2021-01-01")
data['Close'].plot(title="AAPL Stock Price in 2020")
print(data.head())
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Close'], label='AAPL Close Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('AAPL Stock Price in 2020')
plt.legend()
plt.grid()
plt.show()