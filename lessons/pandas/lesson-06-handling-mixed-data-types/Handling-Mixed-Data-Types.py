import pandas as pd

df = pd.DataFrame({
    'A': [1, 'two', 3, 4.0],
    'B': ['10', 20, '30', 40]
})

# Convert to a single type
df['A'] = pd.to_numeric(df['A'], errors='coerce')
df['B'] = pd.to_numeric(df['B'], errors='coerce')
print(df)