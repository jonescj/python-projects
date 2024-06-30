import pandas as pd

df = pd.DataFrame({
    'A': ['foo', 'foo', 'bar', 'bar'],
    'B': ['one', 'two', 'one', 'two'],
    'C': [1, 2, 3, 4],
    'D': [10, 20, 30, 40]
})

# Apply multiple functions to a group
grouped = df.groupby('A').agg({
    'C': ['sum', 'mean'],
    'D': ['min', 'max']
})
print(grouped)