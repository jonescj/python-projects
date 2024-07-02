import pandas as pd

import requests

# Fetch data from an API
response = requests.get('https://api.example.com/data')
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data)
print(df)

# Export to JSON
df.to_json('output.json', orient='records', lines=True)

# Export to HTML
df.to_html('output.html')

# Export to HDF5
df.to_hdf('output.h5', key='df', mode='w')