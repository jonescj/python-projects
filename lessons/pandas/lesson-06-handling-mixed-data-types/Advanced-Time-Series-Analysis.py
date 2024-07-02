import pandas as pd

# Creating a period range
pr = pd.period_range(start='2020-01-01', end='2020-12-31', freq='M')
print(pr)

# Creating a DataFrame with periods
df = pd.DataFrame({
    'Period': pr,
    'Value': range(len(pr))
})
print(df)

# Creating a time delta
td = pd.to_timedelta(['1 days', '2 days', '3 days'])
print(td)

# Using time deltas in a DataFrame
df = pd.DataFrame({
    'Start': pd.date_range('2020-01-01', periods=3),
    'End': pd.date_range('2020-01-02', periods=3)
})
df['Duration'] = df['End'] - df['Start']
print(df)