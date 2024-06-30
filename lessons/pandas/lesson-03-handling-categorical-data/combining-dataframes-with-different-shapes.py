import pandas as pd

df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
})

df2 = pd.DataFrame({
    'C': ['C0', 'C1'],
    'D': ['D0', 'D1']
}, index=[1, 2])
print(df2)

# Join DataFrames
result = df1.join(df2, how='outer')
print(result)
