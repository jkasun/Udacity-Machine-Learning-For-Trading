import pandas as pd
import matplotlib.pyplot as plt

start_date = '2017-01-01'
end_date = '2018-06-21'
dates = pd.date_range(start_date, end_date)
df1 = pd.DataFrame(index=dates)

dfIBM = pd.read_csv(
    "../data/IBM.csv",
    index_col="Date",
    parse_dates=True,
    usecols=["Date", "Adj Close"],
    na_values=['nan']
)

dfIBM = dfIBM.rename(columns={"Adj Close": "IBM"})

df1 = df1.join(dfIBM, how="inner")

symbols = ['AAPL', 'AMZN', 'FB']

for symbol in symbols:
    df_temp = pd.read_csv(
        "../data/{}.csv".format(symbol),
        index_col="Date",
        parse_dates=True,
        usecols=["Date", "Adj Close"],
        na_values=['nan']
    )

    df_temp = df_temp.rename(columns={'Adj Close': symbol})
    df1 = df1.join(df_temp)

"""
Normalize the data
pandas will divide the all price indexes from its starting value
"""
df1 = df1 / df1.ix[0,:]

# Plotting the data
ax = df1.plot(title="Stock Prices")
ax.set_xlabel("Date")
ax.set_ylabel("Price")
plt.show()
