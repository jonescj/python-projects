import pandas as pd

import swifter

# Creating a sample DataFrame
df = pd.DataFrame({
    'A': np.random.randint(0, 100, size=1000000),
    'B': np.random.randint(0, 100, size=1000000)
})

# Using swifter to apply a function in parallel
df['A_squared'] = df['A'].swifter.apply(lambda x: x**2)
print(df.head())