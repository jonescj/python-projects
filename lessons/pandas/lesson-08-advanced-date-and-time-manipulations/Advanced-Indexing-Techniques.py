import pandas as pd

df = pd.DataFrame({
    'A': ['foo', 'foo', 'bar', 'bar'],
    'B': ['one', 'two', 'one', 'two'],
    'C': [1, 2, 3, 4]
})

# Setting MultiIndex
df.set_index(['A', 'B'], inplace=True)
print(df)

# Resetting the index
df_reset = df.reset_index()
print(df_reset)