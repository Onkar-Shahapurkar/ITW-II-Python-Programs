import numpy as np

array_to_sort = np.array([13, 45, 46, 48, 34, 86, 12, 45])
sub_arrays = np.array_split(array_to_sort, 4)
print("\nSub-arrays:")

for i, sub_array in enumerate(sub_arrays):
    print(f"Sub-array {i + 1}: {sub_array}")
