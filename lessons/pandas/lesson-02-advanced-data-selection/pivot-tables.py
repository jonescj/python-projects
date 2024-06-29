import pandas as pd

df = pd.DataFrame({
    'A': ['foo', 'foo', 'bar', 'bar'],
    'B': ['one', 'two', 'one', 'two'],
    'C': ['small', 'large', 'small', 'large'],
    'D': [1, 2, 3, 4]
})

pivot_table = df.pivot_table(values='D', index=['A', 'B'], columns=['C'], aggfunc='sum', fill_value=0)
print(pivot_table)
