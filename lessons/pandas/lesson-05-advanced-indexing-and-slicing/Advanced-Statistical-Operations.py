import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': np.random.randn(1000),
    'B': np.random.rand(1000)
})

# Custom percentiles
desc = df.describe(percentiles=[.05, .25, .75, .95])
print(desc)

# Correlation matrix
corr = df.corr()
print(corr)

# Covariance matrix
cov = df.cov()
print(cov)