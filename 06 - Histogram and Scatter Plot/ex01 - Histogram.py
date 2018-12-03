from libs.stockdata import getStockData
import matplotlib.pyplot as plt

df = getStockData()

df_daliy_return = (df / df.shift(1)) - 1
df_daliy_return.ix[0, :] = 0

dr_fb = df_daliy_return.loc[:, ['FB']]

dr_fb.hist(bins=40)

mean = dr_fb['FB'].mean()
std = dr_fb['FB'].std()

plt.axvline(mean, color='black', linestyle='dashed', linewidth=2)
plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)

plt.show()

print('kurtosis', dr_fb.kurtosis())

# if kurtosis is positive it has fat tails
# if kurtosis is negative it has thin tails
