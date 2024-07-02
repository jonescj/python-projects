import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 5

broadcasted_sum = array + scalar  # Broadcasting the scalar to each element
print(broadcasted_sum)