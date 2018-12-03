from libs.stockdata import getStockData
import matplotlib.pyplot as plt

df = getStockData()

daliy_returns = (df / df.shift(1)) - 1
daliy_returns.ix[0, :] = 0

daliy_returns['IBM'].hist(bins=40, label='IBM')
daliy_returns['FB'].hist(bins=40, label='Facebook')

plt.show()