import numpy as np

arr1 = np.array([5, 10, 15, 20, 25])

print("Array:", arr1)
print("Shape:", arr1.shape)
print("Dimensions:", arr1.ndim)
print("Size:", arr1.size)
print("Data type:", arr1.dtype)

arr_add10 = arr1 + 10
print("Add 10 to every element:", arr_add10)

arr_mul3 = arr1 * 3
print("Multiply every element by 3:", arr_mul3)

print("Sum:", arr1.sum())
print("Mean:", arr1.mean())
print("Maximum:", arr1.max())
print("Minimum:", arr1.min())

arr2 = np.array([2, 4, 6, 8, 10])

print("Element-wise Addition:", arr1 + arr2)
print("Element-wise Subtraction:", arr1 - arr2)
print("Element-wise Multiplication:", arr1 * arr2)
print("Element-wise Division:", arr1 / arr2)
