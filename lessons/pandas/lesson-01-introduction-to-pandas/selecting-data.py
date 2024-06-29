import pandas as pd

# Creating a DataFrame
df = pd.read_csv('data.csv')

# Selecting a single column
print(df['Name'])

# Selecting multiple columns
print(df[['Name', 'Age']])

# Selecting rows by index
print(df.iloc[0])       # First row
print(df.iloc[0:3])     # First three rows

# Selecting rows by condition
print(df[df['Age'] > 30])
