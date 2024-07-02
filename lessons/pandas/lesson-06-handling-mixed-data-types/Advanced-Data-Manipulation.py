import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Using .at for label-based scalar access
print(df.at[1, 'A'])

# Using .iat for position-based scalar access
print(df.iat[1, 1])