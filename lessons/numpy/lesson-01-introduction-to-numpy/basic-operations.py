import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

elementwise_sum = array1 + array2    # Element-wise addition
print(elementwise_sum)

elementwise_product = array1 * array2 # Element-wise multiplication
print(elementwise_product)

matrix_product = np.dot(array1, array2) # Dot product
print(matrix_product)