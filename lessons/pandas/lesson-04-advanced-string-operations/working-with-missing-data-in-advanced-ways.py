import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [10, 20, 30, np.nan, 50]
})

# Interpolate missing data
df_interpolated = df.interpolate()
print(df_interpolated)

# Forward fill
df_ffill = df.ffill()
print(df_ffill)

# Backward fill
df_bfill = df.bfill()
print(df_bfill)