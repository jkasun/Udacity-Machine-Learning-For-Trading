import pandas as pd

def test_run():
    df = pd.read_csv("../data/AAPL.csv")
    print (df.head())

if __name__ == "__main__":
    test_run()