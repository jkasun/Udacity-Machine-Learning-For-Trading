from libs.stockdata import getStockData
import matplotlib.pyplot as plt
import numpy as np

df = getStockData()

daliy_returns = (df / df.shift(1)) - 1
daliy_returns.ix[0, :] = 0

daliy_returns.plot(kind='scatter', x='FB', y='SPY')
beta_facebook, alpha_facebook = np.polyfit(daliy_returns['SPY'], daliy_returns['FB'], 1)
plt.plot(daliy_returns['SPY'], beta_facebook * daliy_returns['SPY'] + alpha_facebook, '-', color='r')
plt.show()

daliy_returns.plot(kind='scatter', x='AAPL', y='SPY')
beta_apple, aplha_apple = np.polyfit(daliy_returns['SPY'], daliy_returns['AAPL'], 1)
plt.plot(daliy_returns['SPY'], beta_apple * daliy_returns['SPY'] + aplha_apple, '-', color='r')
plt.show()