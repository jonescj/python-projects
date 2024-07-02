import pandas as pd

df = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Value': np.random.randn(100)
})
df.set_index('Date', inplace=True)

# Custom resampling function
df_resampled = df.resample('M').apply(lambda x: x.sum())
print(df_resampled)