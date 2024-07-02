import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Create a random DataFrame
np.random.seed(42)
df = pd.DataFrame({
    'A': np.random.randn(100),  # 100 random numbers from a normal distribution
    'B': np.random.rand(100)    # 100 random numbers from a uniform distribution
})

# Create SQLAlchemy engine
engine = create_engine('sqlite:///:memory:')

# Write DataFrame to SQL
df.to_sql('table_name', con=engine, index=False)

# Perform SQL query
query = 'SELECT * FROM table_name WHERE A > 2'
result = pd.read_sql(query, con=engine)
print(result)