from libs.stockdata import getStockData
import matplotlib.pyplot as plt
import numpy as np

df = getStockData()

# How closely data fit togeather 
print(df.corr(method='pearson'))