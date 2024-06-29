import pandas as pd

df = pd.DataFrame({
    'Value': [1, 2, 3, 4, 5, 6, 7]
})

# Rolling window calculation
df['RollingMean'] = df['Value'].rolling(window=3).mean()
print(df)

# Expanding window calculation
df['ExpandingSum'] = df['Value'].expanding(min_periods=1).sum()
print(df)
