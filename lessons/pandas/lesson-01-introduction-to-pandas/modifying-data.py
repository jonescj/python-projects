import pandas as pd

# Creating a DataFrame
df = pd.read_csv('data.csv')

# Adding a new column
df['Salary'] = [70000, 80000, 90000, 100000]
print(df)

# Modifying an existing column
df['Age'] = df['Age'] + 1
print(df)

# Dropping a column
df = df.drop(columns=['City'])
print(df)
