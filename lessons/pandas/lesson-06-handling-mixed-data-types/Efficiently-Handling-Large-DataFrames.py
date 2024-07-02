import pandas as pd

df = pd.DataFrame({
    'A': ['foo', 'bar', 'baz'] * 1000,
    'B': [1, 2, 3] * 1000
})

# Convert to categorical
df['A'] = df['A'].astype('category')
print(df.memory_usage(deep=True))

# Creating a sparse DataFrame
df = pd.DataFrame({
    'A': [0, 0, 1, 0, 0],
    'B': [1, 0, 0, 0, 2]
}).astype(pd.SparseDtype("int", 0))

print(df)
print(df.memory_usage(deep=True))