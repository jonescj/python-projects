import pandas as pd

df = pd.DataFrame({
    'A': ['foo', 'foo', 'bar', 'bar'],
    'B': ['one', 'two', 'one', 'two'],
    'C': [1, 3, 2, 4],
    'D': [10, 20, 30, 40]
})

# Multiple aggregations
grouped = df.groupby('A').agg({
    'C': ['mean', 'sum'],
    'D': 'sum'
})
print(grouped)

# Custom aggregation function
def range_func(x):
    return x.max() - x.min()

grouped = df.groupby('A').agg({
    'C': range_func,
    'D': range_func
})
print(grouped)
