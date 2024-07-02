import pandas as pd

df = pd.DataFrame({
    'A': ['foo', 'foo', 'bar', 'bar'],
    'B': ['one', 'two', 'one', 'two'],
    'C': [1, 2, 3, 4],
    'D': [10, 20, 30, 40]
})

# Pivoting with multiple indexes
pivoted = df.pivot_table(index=['A', 'B'], values='C', columns='D', aggfunc='sum', fill_value=0)
print(pivoted)

df = pd.DataFrame({
    'A': [[1, 2, 3], [4, 5, 6]]
})

# Exploding list-like column
df_exploded = df.explode('A')
print(df_exploded)