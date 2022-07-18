# Using resize()
import numpy as np
oneDarray = np.arange(1, 7)
print("Original Array: \n", oneDarray)
print("Size of original array: \n", oneDarray.shape, end = "\n\n")

oneDarray.resize(3, 3)
print("Array after using resize() over it: \n", oneDarray)
print("Dimensions of array after using resize() over it: \n", oneDarray.shape)