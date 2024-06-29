import pandas as pd

# Creating a DataFrame
df = pd.read_csv('data.csv')

# Checking for missing values
print(df.isnull().sum())

# Dropping rows with missing values
df = df.dropna()
print(df)

# Filling missing values
df = df.fillna(value=0)
print(df)
