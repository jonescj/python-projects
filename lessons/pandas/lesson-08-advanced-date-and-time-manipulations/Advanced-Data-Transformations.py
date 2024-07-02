import pandas as pd

# Define a transformation function
def add_one(df):
    return df + 1

# Apply the function using pipe
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df = df.pipe(add_one)
print(df)

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Using assign to add a new column
df = df.assign(C=lambda x: x['A'] + x['B'])
print(df)