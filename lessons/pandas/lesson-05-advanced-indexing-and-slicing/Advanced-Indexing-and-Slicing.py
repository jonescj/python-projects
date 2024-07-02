import pandas as pd

df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
})

# Set a column as index
df.set_index('Name', inplace=True)
print(df)

# Reset index
df.reset_index(inplace=True)
print(df)

# Slicing with loc
print(df.loc[0:2, ['Name', 'Age']])

# Slicing with iloc
print(df.iloc[0:2, 0:2])