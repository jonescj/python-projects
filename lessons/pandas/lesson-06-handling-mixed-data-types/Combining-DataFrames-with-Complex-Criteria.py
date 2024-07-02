import pandas as pd

df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value': [1, 2, 3, 4]
})

df2 = pd.DataFrame({
    'key': ['B', 'D', 'E'],
    'value': [5, 6, 7]
})

# Merge with a conditional
merged = pd.merge(df1, df2, on='key', how='outer', suffixes=('_left', '_right'))
merged['value'] = merged['value_left'].combine_first(merged['value_right'])
merged = merged.drop(columns=['value_left', 'value_right'])
print(merged)