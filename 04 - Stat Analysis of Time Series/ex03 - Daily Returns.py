from libs.stockdata import getStockData
import matplotlib.pyplot as plt
import pandas as pd

df = getStockData()

daily_returns = df.copy()

# Compute daily returns for row 1 onward
# daily_returns[1:] = (df[1:] / df[:-1].values) - 1
# daily_returns.ix[0, :] = 0 # Set daily returns for row 0 to 0

# which is equals to
daily_returns = ( df / df.shift(1)) - 1
daily_returns.ix[0, :] = 0

daily_returns.plot()
plt.show()