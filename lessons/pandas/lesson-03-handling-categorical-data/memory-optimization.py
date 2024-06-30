import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [1.0, 2.0, 3.0, 4.0, 5.0]
})

# Downcasting
df['A'] = pd.to_numeric(df['A'], downcast='integer')
df['B'] = pd.to_numeric(df['B'], downcast='float')
print(df.dtypes)
