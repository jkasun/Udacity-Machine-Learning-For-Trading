from libs.stockdata import getStockData
import matplotlib.pyplot as plt
import pandas as pd

df = getStockData()

# Plot SPY data, retain matplotlib axis object
df_fb = df.loc[:, ['FB']]
ax = df_fb.plot(title='FB rolling mean', label="FB")

# Compute rolling mean using a 20 day window
rolling_mean = df_fb.rolling(20).mean()
rolling_std = df_fb.rolling(20).std()

upper_band = rolling_mean + (2 * rolling_std)
lower_band = rolling_mean - (2 * rolling_std)

# Add rolling mean to same plot
rolling_mean.plot(label='Rolling Mean', ax=ax)
upper_band.plot(label="Upper Band", ax=ax)
lower_band.plot(label="Lower Band", ax=ax)

# Add axis labels and legend
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.legend(loc='upper left')

plt.show()