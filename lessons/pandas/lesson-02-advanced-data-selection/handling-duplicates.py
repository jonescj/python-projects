import pandas as pd

df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
    'B': [1, 2, 1, 2, 1, 2]
})

# Check for duplicates
print(df.duplicated())

# Drop duplicates
df = df.drop_duplicates()
print(df)
