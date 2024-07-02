import pandas as pd

df = pd.DataFrame({
    'info': ['John, Doe, 30', 'Anna, Smith, 25', 'Peter, Pan, 22']
})

# Extracting multiple substrings
df[['FirstName', 'LastName', 'Age']] = df['info'].str.split(', ', expand=True)
print(df)

# Using regular expressions
df['Age'] = df['info'].str.extract(r'(\d+)', expand=False)
print(df)