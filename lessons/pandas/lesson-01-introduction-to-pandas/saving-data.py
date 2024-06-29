import pandas as pd

# Creating a DataFrame
df = pd.read_csv('data.csv')
df.to_csv('output.csv', index=False)
