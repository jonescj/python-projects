import pandas as pd
import dask.dataframe as dd

# Load a large CSV file with Dask
df = dd.read_csv('large_data.csv')

# Perform operations with Dask DataFrame
result = df.groupby('Column1').sum().compute()
print(result)

'''
# Configuration
num_rows=1000000  # Number of rows
num_cols=10       # Number of columns

# Generate header
header=$(seq -s, 1 $num_cols | sed 's/[0-9]*/Column&/g')

# Generate data and write to CSV file
(echo $header; awk -v rows=$num_rows -v cols=$num_cols 'BEGIN {
    srand();
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            printf "%d", int(1 + rand() * 100);
            if (j < cols - 1) {
                printf ",";
            }
        }
        printf "\n";
    }
}') > large_data.csv

'''