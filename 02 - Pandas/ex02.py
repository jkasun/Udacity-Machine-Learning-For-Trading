import pandas as pd

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

# SLICING DATA
sd = '2017-06-01'
ed = '2017-06-05'
df2 = df1.loc[sd:ed, ['AAPL', 'FB']]
print(df2)

# Slice by Row
df_row_slice = df1.ix[sd: ed]
print(df_row_slice)

# Slice by Col
df_col_slice = df1[['IBM', 'FB']]
print(df_col_slice)

# Slice by row and col
df_row_col = df1.ix[sd: ed, ['IBM', 'FB']]
print(df_row_col)
