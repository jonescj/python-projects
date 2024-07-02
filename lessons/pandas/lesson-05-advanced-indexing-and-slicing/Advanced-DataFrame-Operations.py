import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
})

# Query DataFrame
result = df.query('A > 2 and B < 40')
print(result)

# Evaluate expressions
df['C'] = df.eval('A + B')
print(df)