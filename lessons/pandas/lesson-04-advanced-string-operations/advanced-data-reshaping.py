import pandas as pd

df = pd.DataFrame({
    'A': ['foo', 'foo', 'bar', 'bar'],
    'B': ['one', 'two', 'one', 'two'],
    'C': ['small', 'large', 'small', 'large'],
    'D': [1, 2, 3, 4]
})

# Set index and reshape
df = df.set_index(['A', 'B', 'C'])
print(df)

# Stack and unstack
stacked = df.stack()
print(stacked)

unstacked = stacked.unstack()
print(unstacked)