from libs.stockdata import getStockData
import matplotlib.pyplot as plt
import pandas as pd

df = getStockData()

cumulative_returns = (df / df.ix[0]) -1

cumulative_returns.plot()
plt.show()