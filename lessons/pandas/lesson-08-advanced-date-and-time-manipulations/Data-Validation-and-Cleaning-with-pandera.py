import pandas as pd

import pandera as pa
from pandera import Column

# Define a schema
schema = pa.DataFrameSchema({
    "column1": Column(pa.String, checks=pa.Check(lambda s: s.str.startswith("A"))),
    "column2": Column(pa.Int, checks=pa.Check.ge(0)),
})

# Validate a DataFrame
df = pd.DataFrame({"column1": ["A1", "A2", "A3"], "column2": [1, 2, 3]})
validated_df = schema.validate(df)
print(validated_df)