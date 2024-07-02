import pandas as pd

df = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Value': np.random.randn(10)
})
df.set_index('Date', inplace=True)

# Rolling window calculations
df['RollingMean'] = df['Value'].rolling(window=3).mean()
print(df)

# Expanding window calculations
df['ExpandingSum'] = df['Value'].expanding().sum()
print(df)