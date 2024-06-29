import pandas as pd

# Applying a function to a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30]
})

def add_ten(x):
    return x + 10

df['A'] = df['A'].apply(add_ten)
print(df)

# Applying a function to multiple columns
df['C'] = df.apply(lambda row: row['A'] + row['B'], axis=1)
print(df)

# Applying a function to each element of the DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30]
})

df = df.applymap(lambda x: x * 2)
print(df)
