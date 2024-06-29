import pandas as pd

# Creating a DataFrame
df = pd.read_csv('data.csv')
print(df.head())        # Display the first 5 rows
print(df.tail())        # Display the last 5 rows
print(df.info())        # Summary of the DataFrame
print(df.describe())    # Statistical summary of numerical columns
