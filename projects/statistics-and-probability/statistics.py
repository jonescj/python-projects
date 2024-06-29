from collections import Counter
import math

# Mean
def mean_list(data):
    return sum(data) / len(data)

def mean_lambda(data, func):
    return sum(func(x) for x in data) / len(data)

# Median
def median_list(data):
    data = sorted(data)
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]

def median_lambda(data, func):
    transformed_data = sorted(func(x) for x in data)
    n = len(transformed_data)
    mid = n // 2
    if n % 2 == 0:
        return (transformed_data[mid - 1] + transformed_data[mid]) / 2
    else:
        return transformed_data[mid]

# Mode
def mode_list(data):
    count = Counter(data)
    max_freq = max(count.values())
    modes = [key for key, freq in count.items() if freq == max_freq]
    return modes

def mode_lambda(data, func):
    transformed_data = [func(x) for x in data]
    count = Counter(transformed_data)
    max_freq = max(count.values())
    modes = [key for key, freq in count.items() if freq == max_freq]
    return modes

# Range
def range_list(data):
    return max(data) - min(data)

def range_lambda(data, func):
    transformed_data = [func(x) for x in data]
    return max(transformed_data) - min(transformed_data)

# Variance
def variance_list(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def variance_lambda(data, func):
    transformed_data = [func(x) for x in data]
    mean = sum(transformed_data) / len(transformed_data)
    return sum((x - mean) ** 2 for x in transformed_data) / len(transformed_data)

# Standard Deviation
def stddev_list(data):
    return math.sqrt(variance_list(data))

def stddev_lambda(data, func):
    return math.sqrt(variance_lambda(data, func))

# Example Usage
data = [1, 2, 2, 3, 4]

print("Mean (list):", mean_list(data))
print("Mean (lambda):", mean_lambda(data, lambda x: x))

print("Median (list):", median_list(data))
print("Median (lambda):", median_lambda(data, lambda x: x))

print("Mode (list):", mode_list(data))
print("Mode (lambda):", mode_lambda(data, lambda x: x))

print("Range (list):", range_list(data))
print("Range (lambda):", range_lambda(data, lambda x: x))

print("Variance (list):", variance_list(data))
print("Variance (lambda):", variance_lambda(data, lambda x: x))

print("Standard Deviation (list):", stddev_list(data))
print("Standard Deviation (lambda):", stddev_lambda(data, lambda x: x))
