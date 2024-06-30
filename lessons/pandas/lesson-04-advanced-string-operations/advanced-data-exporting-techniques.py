import pandas as pd
from sqlalchemy import create_engine

with pd.ExcelWriter('output.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet1')
    df.to_excel(writer, sheet_name='Sheet2')

# Create SQLAlchemy engine
engine = create_engine('sqlite:///:memory:')

# Export DataFrame to SQL database
df.to_sql('table_name', con=engine, index=False)