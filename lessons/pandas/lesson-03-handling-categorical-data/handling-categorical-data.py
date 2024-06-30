import pandas as pd

df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'City': ['New York', 'Paris', 'Berlin', 'London']
})
print(df)

# Convert to categorical
df['City'] = df['City'].astype('category')
print(df)

# Get categories
print(df['City'].cat.categories)

# Define the mapping of original to new categories
category_mapping = {
    'New York': 'NYC',
    'Paris': 'PAR',
    'Berlin': 'BER',
    'London': 'LDN'
}

# Apply the mapping
df['City'] = df['City'].apply(lambda x: category_mapping[x])
print(df)