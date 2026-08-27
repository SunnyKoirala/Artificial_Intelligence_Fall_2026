import numpy as np

# 1. Create a 1D NumPy array
arr1 = np.array([5, 10, 15, 20, 25])

# 2. Display array properties
print("Array:", arr1)
print("Shape:", arr1.shape)
print("Number of dimensions:", arr1.ndim)
print("Size:", arr1.size)
print("Data type:", arr1.dtype)

# 3. Add 10 to every element
print("\nArray + 10:", arr1 + 10)

# 4. Multiply every element by 3
print("Array * 3:", arr1 * 3)

# 5. Find Sum, Mean, Maximum and Minimum
print("\nSum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Maximum:", np.max(arr1))
print("Minimum:", np.min(arr1))

# 6. Create another array
arr2 = np.array([2, 4, 6, 8, 10])

print("\nSecond Array:", arr2)

# 7. Element-wise operations
print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)