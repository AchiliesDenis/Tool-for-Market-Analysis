

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download historical data
data = yf.download("EURUSD=X", start="2023-01-01", end="2024-01-01")

# Calculate moving averages
data['MA20'] = data['Close'].rolling(20).mean()
data['MA50'] = data['Close'].rolling(50).mean()

# Simple buy/sell signal
data['Signal'] = 0
data.loc[data['MA20'] > data['MA50'], 'Signal'] = 1
data.loc[data['MA20'] < data['MA50'], 'Signal'] = -1

# Print last 5 rows
print(data[['Close', 'MA20', 'MA50', 'Signal']].tail())

# Plot
plt.figure(figsize=(10,5))
plt.plot(data['Close'], label='Close Price')
plt.plot(data['MA20'], label='MA20')
plt.plot(data['MA50'], label='MA50')
plt.legend()
plt.show()
