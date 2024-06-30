import pandas as pd

df = pd.DataFrame({
    'Email': ['john.doe@example.com', 'anna.smith@sample.org', 'peter.pan@test.net']
})

# Extract domain names
df['Domain'] = df['Email'].str.extract(r'@([^\.]+)\.')
print(df)

# Split email into username and domain
df[['Username', 'Domain']] = df['Email'].str.split('@', expand=True)
print(df)

# Check if email contains 'example'
df['ContainsExample'] = df['Email'].str.contains('example')
print(df)