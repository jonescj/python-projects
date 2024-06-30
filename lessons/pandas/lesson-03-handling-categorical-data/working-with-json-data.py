import pandas as pd

json_data = '''
[
    {"Name": "John", "Age": 28, "City": "New York"},
    {"Name": "Anna", "Age": 24, "City": "Paris"},
    {"Name": "Peter", "Age": 35, "City": "Berlin"}
]
'''

# Load JSON data into a DataFrame
df = pd.read_json(json_data)
print(df)
