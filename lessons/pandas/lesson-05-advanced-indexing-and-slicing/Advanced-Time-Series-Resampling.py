import pandas as pd

df = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=24, freq='h'),
    'Value': range(24)
})
df.set_index('Date', inplace=True)

# Resample to daily frequency
daily = df.resample('D').sum()
print(daily)

# Resample to minute frequency
minute = df.resample('min').sum()
print(minute)

# Custom resampling with a custom function
custom_resample = df.resample('D').apply(lambda x: x.max() - x.min())
print(custom_resample)