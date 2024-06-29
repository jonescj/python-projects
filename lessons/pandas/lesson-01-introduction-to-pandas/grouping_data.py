import pandas as pd

# Creating a DataFrame
df = pd.read_csv('data.csv')

# Grouping by a column
grouped = df.groupby('City')

# Aggregating data
print(grouped['Age'].mean())
print(grouped['Salary'].sum())
