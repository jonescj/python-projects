import pandas as pd

# Custom aggregation function
def custom_agg(x):
    return x.max() - x.min()

grouped = df.groupby('A').agg({
    'C': custom_agg,
    'D': custom_agg
})
print(grouped)