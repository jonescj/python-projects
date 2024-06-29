import pandas as pd

# Creating a DataFrame
df = pd.read_csv('data.csv')

# Using loc
print(df.loc[0])            # First row by label
print(df.loc[0:2, 'Name'])  # Rows 0 to 2 for the 'Name' column

# Using iloc
print(df.iloc[0])           # First row by position
print(df.iloc[0:2, 0])      # Rows 0 to 2 for the first column
