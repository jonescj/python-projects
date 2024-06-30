import pandas as pd

# Creating a MultiIndex DataFrame
arrays = [
    ['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
    ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']
]

index = pd.MultiIndex.from_arrays(arrays, names=('first', 'second'))
print(index)

df = pd.DataFrame({'A': range(8), 'B': range(8, 16)}, index=index)
print(df)

# Accessing data in a MultiIndex DataFrame
print(df.loc['bar'])
print(df.loc['bar', 'one'])
