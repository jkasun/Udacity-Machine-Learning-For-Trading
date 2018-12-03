import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/AAPL.csv")
df[20:100][['Close', 'Adj Close']].plot()
plt.show()