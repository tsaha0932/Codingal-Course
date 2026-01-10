import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.arange(1, 7).reshape(1, 6)
print(f"Array 1: {arr1}")
print(f"Array 2 (reshaped): {arr2}\n")

print(f"Addition (arr1 + arr2): {arr1 + arr2}")
print(f"Multiplication (arr1 * arr2): {arr1 * arr2}")
print(f"Division (arr1 / arr2): {arr1 / arr2}")
print(f"Power (arr1 ** 2): {arr1 ** 2}\n")

arr3 = np.array([70, 80, 90])
arr_joined = np.concatenate((arr1, arr3))
print(f"Joined array (concatenate): {arr_joined}")

arr_unsorted = np.array([3, 1, 4, 2])
print(f"Sorted array: {np.sort(arr_unsorted)}\n")

print(f"First element of arr1: {arr1[0]}")
print(f"Elements from index 1 to 4 of arr1 (slicing): {arr1[1:5]}")