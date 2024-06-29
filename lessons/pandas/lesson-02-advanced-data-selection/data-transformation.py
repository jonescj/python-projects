import pandas as pd

df = pd.DataFrame({
    'A': [3, 2, 1],
    'B': [30, 20, 10]
})

# Sorting by a single column
df = df.sort_values(by='A')
print(df)

# Sorting by multiple columns
df = df.sort_values(by=['A', 'B'])
print(df)

df = pd.DataFrame({
    'A': ['1', '2', '3'],
    'B': ['10.1', '20.2', '30.3']
})

# Convert data types
df['A'] = df['A'].astype(int)
df['B'] = df['B'].astype(float)
print(df.dtypes)
