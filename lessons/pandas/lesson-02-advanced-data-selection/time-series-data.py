import pandas as pd

date_range = pd.date_range(start='1/1/2020', end='1/08/2020')
print(date_range)

ts_df = pd.DataFrame({
    'Date': pd.date_range(start='1/1/2020', periods=7),
    'Value': [1, 2, 3, 4, 5, 6, 7]
})
ts_df.set_index('Date', inplace=True)
print(ts_df)

# Resample to daily frequency
daily = ts_df.resample('D').sum()
print(daily)

# Resample to weekly frequency
weekly = ts_df.resample('W').sum()
print(weekly)
