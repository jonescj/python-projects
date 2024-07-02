import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
})

# Apply a function to a column
df['A_squared'] = df['A'].apply(lambda x: x**2)
print(df)

# Apply a function to rows
df['sum_AB'] = df.apply(lambda row: row['A'] + row['B'], axis=1)
print(df)