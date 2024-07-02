import pandas as pd

arrays = [
    ['bar', 'bar', 'baz', 'baz'],
    ['one', 'two', 'one', 'two']
]
index = pd.MultiIndex.from_arrays(arrays, names=('first', 'second'))
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}, index=index)
print(df)

# Accessing data in a MultiIndex DataFrame
print(df.loc['bar'])
print(df.loc[('bar', 'one')])