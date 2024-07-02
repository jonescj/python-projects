import pandas as pd

import dask.dataframe as dd

# Load a large CSV file with Dask
df = dd.read_csv('large_data.csv')

# Perform operations with Dask DataFrame
result = df.groupby('column_name').sum().compute()
print(result)

