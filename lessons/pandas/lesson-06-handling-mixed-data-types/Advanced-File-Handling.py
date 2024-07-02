import pandas as pd

# Reading a compressed CSV file
df = pd.read_csv('data.csv.gz', compression='gzip')
print(df.head())

# Writing to a compressed CSV file
df.to_csv('data_compressed.csv.gz', compression='gzip')