import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1]
})

# Rank
df['Rank'] = df['A'].rank()
print(df)

# Percent rank
df['PercentRank'] = df['A'].rank(pct=True)
print(df)

# Expanding sum
df['ExpandingSum'] = df['A'].expanding().sum()
print(df)