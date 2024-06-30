import pandas as pd

df1 = pd.DataFrame({
    'key1': ['K0', 'K1', 'K2'],
    'key2': ['K0', 'K1', 'K0'],
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
})

df2 = pd.DataFrame({
    'key1': ['K0', 'K1', 'K2'],
    'key2': ['K0', 'K0', 'K0'],
    'C': ['C0', 'C1', 'C2'],
    'D': ['D0', 'D1', 'D2']
})

# Merge on multiple keys
result = pd.merge(df1, df2, on=['key1', 'key2'])
print(result)

df1 = pd.DataFrame({'value': ['K0', 'K1', 'K2']})
df2 = pd.DataFrame({'value': [1, 2, 3]})

print(df1)
print(df2)

# Perform cross join
df1['key'] = 1
df2['key'] = 1

print(df1)
print(df2)

result = pd.merge(df1, df2, on='key').drop('key', axis=1)
print(result)