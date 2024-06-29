import pandas as pd

df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', 'Linda']
})

# Converting to lowercase
df['Name'] = df['Name'].str.lower()
print(df)

# Checking for substrings
df['Contains_a'] = df['Name'].str.contains('a')
print(df)

# Replacing substrings
df['Name'] = df['Name'].str.replace('a', 'x')
print(df)
