
import numpy as np

oneDarray = np.linspace(1, 6, 6, dtype = int)
print("Original Array: \n", oneDarray)
print("Size of original array: \n", oneDarray.shape, end = "\n\n")


# Using reshape()

NDarray = np.reshape(oneDarray, (2,3))
print("Array after using reshape() over it: \n", NDarray)
print("Dimensions of array after using reshape() over it: \n", NDarray.shape, end = "\n\n")