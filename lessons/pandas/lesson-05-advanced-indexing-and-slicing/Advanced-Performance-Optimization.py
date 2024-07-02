import pandas as pd
import numpy as np
from numba import jit

# Convert DataFrame column to a NumPy array
@jit(nopython=True)
def sum_numba(array):
    return array.sum()

df = pd.DataFrame({
    'A': np.random.randn(1000000)
})

# Apply JIT compiled function
result = sum_numba(df['A'].values)
print(result)
