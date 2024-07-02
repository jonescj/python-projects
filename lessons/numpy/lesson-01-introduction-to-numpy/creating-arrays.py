import numpy as np

array_from_list = np.array([1, 2, 3, 4, 5])
print(array_from_list)

array_from_tuple = np.array((1, 2, 3, 4, 5))
print(array_from_tuple)

zeros_array = np.zeros((2, 3))    # 2x3 array of zeros
print(zeros_array)

ones_array = np.ones((2, 3))      # 2x3 array of ones
print(ones_array)

empty_array = np.empty((2, 3))    # 2x3 array with uninitialized values
print(empty_array)

arange_array = np.arange(0, 10, 2) # Array with values from 0 to 10 with step 2
print(arange_array)

linspace_array = np.linspace(0, 1, 5) # 5 values evenly spaced between 0 and 1
print(linspace_array)