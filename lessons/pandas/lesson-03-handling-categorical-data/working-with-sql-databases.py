import pandas as pd
from sqlalchemy import create_engine

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [1.0, 2.0, 3.0, 4.0, 5.0]
})

# Create an in-memory SQLite database
engine = create_engine('sqlite:///:memory:')
df.to_sql('data', engine)

# Read from SQL database
df_sql = pd.read_sql('data', con=engine)
print(df_sql)
