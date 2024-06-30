import pandas as pd

# Reading large CSV in chunks
chunk_size = 1000
chunks = []

for chunk in pd.read_csv('large_data.csv', chunksize=chunk_size):
    chunks.append(chunk)

df = pd.concat(chunks, axis=0)
print(df)

# Using memory map for large CSV files
df = pd.read_csv('large_data.csv', memory_map=True)
print(df)