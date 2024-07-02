import numpy as np

array = np.array([1, 2, 3, 4, 5])
boolean_index = array > 3

filtered_array = array[boolean_index] # Only elements greater than 3
print(filtered_array)