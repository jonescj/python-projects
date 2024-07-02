import pandas as pd

from numba import jit
import numpy as np

# Define a function and use jit
@jit
def sum_large_array(arr):
    total = 0
    for i in arr:
        total += i
    return total

# Applying the function
arr = np.random.randn(1000000)
print(sum_large_array(arr))