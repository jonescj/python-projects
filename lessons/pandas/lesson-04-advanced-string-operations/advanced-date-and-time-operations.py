import pandas as pd

# Create a date range
date_range = pd.date_range(start='2023-01-01', periods=10, freq='D')
print(date_range)

# Localize and convert time zones
df = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
    'Value': [1, 2, 3, 4, 5]
})

df['Date'] = df['Date'].dt.tz_localize('UTC').dt.tz_convert('US/Eastern')
print(df)