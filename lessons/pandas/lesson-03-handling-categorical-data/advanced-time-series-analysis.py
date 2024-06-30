import pandas as pd

df = pd.DataFrame({
    'Date': pd.date_range(start='1/1/2020', periods=5),
    'Value': [1, 2, 3, 4, 5]
})
df.set_index('Date', inplace=True)

# Shifting data
df['Shifted'] = df['Value'].shift(1)
print(df)

# Rolling window with custom function
df['RollingSum'] = df['Value'].rolling(window=2).apply(lambda x: x.sum())
print(df)
