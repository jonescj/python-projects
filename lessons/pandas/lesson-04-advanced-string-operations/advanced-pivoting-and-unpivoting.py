import pandas as pd

df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter'],
    'Math': [90, 80, 85],
    'Science': [95, 85, 80]
})

# Unpivot the DataFrame
melted = pd.melt(df, id_vars=['Name'], var_name='Subject', value_name='Score')
print(melted)

# Pivot the DataFrame
pivoted = melted.pivot(index='Name', columns='Subject', values='Score')
print(pivoted)