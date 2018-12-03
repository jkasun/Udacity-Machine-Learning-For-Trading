import pandas as pd
import matplotlib.pyplot as plt

def getStockData():
    start_date = '2018-01-01'
    end_date = '2018-06-30'
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

    symbols = ['AAPL', 'AMZN', 'FB', 'SPY']

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

    return df1