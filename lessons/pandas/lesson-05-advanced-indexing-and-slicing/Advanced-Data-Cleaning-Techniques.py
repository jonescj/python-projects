import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Value': [1, 2, 3, 100, 5, 6, 7]
})

# Remove outliers
df_cleaned = df[(df['Value'] - df['Value'].mean()).abs() <= 3 * df['Value'].std()]
print(df_cleaned)

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [10, 20, 30, np.nan, 50]
})

# Fill missing data with mean
df_filled = df.fillna(df.mean())
print(df_filled)

# Drop rows with missing data
df_dropped = df.dropna()
print(df_dropped)