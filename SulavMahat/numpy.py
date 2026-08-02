import numpy as np

# Create a 1D NumPy array
arr = np.array([5, 10, 15, 20, 25])

print("Array:", arr)
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Size:", arr.size)
print("Data Type:", arr.dtype)

# Add 10 to every element
print("\nAfter adding 10:")
print(arr + 10)

# Multiply every element by 3
print("\nAfter multiplying by 3:")
print(arr * 3)

# Find sum, mean, maximum, and minimum
print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Create another array
arr2 = np.array([2, 4, 6, 8, 10])

# Element-wise operations
print("\nSecond Array:", arr2)

print("\nAddition:")
print(arr + arr2)

print("\nSubtraction:")
print(arr - arr2)

print("\nMultiplication:")
print(arr * arr2)

print("\nDivision:")
print(arr / arr2)
