import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])

reshaped_array = array.reshape((3, 2)) # Reshape to 3x2 array
print(reshaped_array)

flattened_array = array.flatten()      # Flatten the array
print(flattened_array)

# Slicing
slice_array = array[0:2, 1:3] # Slicing rows and columns
print(slice_array)