from libs.stockdata import getStockData
import matplotlib.pyplot as plt

df = getStockData()

df.plot()
plt.show()

print('MEAN:\n')
print(df.mean()) # Average total + number of data

print('\nMEDIAN:\n')
print(df.median()) # The middle when sorted

print('\nSTD:\n')
print(df.std())

