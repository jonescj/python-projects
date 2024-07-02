import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [10, 20, 30, np.nan, 50]
})

# Interpolating missing data
df_interpolated = df.interpolate(method='linear')
print(df_interpolated)

# Interpolating with different methods
df_interpolated_time = df.interpolate(method='time')
print(df_interpolated_time)