import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']})
df2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'], 'B': ['B3', 'B4', 'B5']})

# Concatenate along rows
result = pd.concat([df1, df2])
print(result)

# Concatenate along columns
result = pd.concat([df1, df2], axis=1)
print(result)

left = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'A': ['A0', 'A1', 'A2']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K3'], 'B': ['B0', 'B1', 'B3']})

# Merge DataFrames
result = pd.merge(left, right, on='key')
print(result)

