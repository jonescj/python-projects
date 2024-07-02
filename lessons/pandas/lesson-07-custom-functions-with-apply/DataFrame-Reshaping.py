import pandas as pd

df = pd.DataFrame({
    'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
    'B': ['one', 'one', 'two', 'two', 'one', 'one'],
    'C': ['small', 'large', 'small', 'small', 'small', 'large'],
    'D': [1, 2, 3, 4, 5, 6]
})

# Creating a pivot table
pivot_table = df.pivot_table(values='D', index=['A', 'B'], columns=['C'], aggfunc='sum', fill_value=0)
print(pivot_table)