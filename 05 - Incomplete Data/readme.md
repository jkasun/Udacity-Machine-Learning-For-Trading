# Incomplete Data #

## Resources ##

* [pandas Documentation](http://pandas.pydata.org/pandas-docs/stable/)
* [pandas fillna](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.fillna.html?highlight=fillna#pandas.DataFrame.fillna)


```python
def fill_missing_values(df_data):
    df_data.fillna(method='ffill', axis=0, inplace=True)
    df_data.fillna(method='bfill', axis=0, inplace=True)
```