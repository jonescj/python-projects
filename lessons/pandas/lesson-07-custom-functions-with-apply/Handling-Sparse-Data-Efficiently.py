import pandas as pd

# Creating a sparse DataFrame
df = pd.DataFrame({
    'A': [0, 0, 1, 0, 0],
    'B': [1, 0, 0, 0, 2]
}).astype(pd.SparseDtype("int", 0))

print(df)
print(df.memory_usage(deep=True))