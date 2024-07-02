import pandas as pd

df = pd.DataFrame({
    'key': ['A', 'B', 'A', 'B'],
    'value': [1, 2, 3, 4]
})

# Group by and apply transform
df['transformed'] = df.groupby('key')['value'].transform(lambda x: x - x.mean())
print(df)

# Filter groups based on a condition
filtered = df.groupby('key').filter(lambda x: x['value'].mean() > 2)
print(filtered)