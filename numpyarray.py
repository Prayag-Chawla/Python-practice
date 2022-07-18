import numpy as np

# array() creates array of the passed list

# array_1 = np.array([1, 2, 3, 4])
# print(array_1)
# print(type(array_1), end = "\n\n\n")





array_1 = np.array([1, 2.5, '3', 'abc'])
print(array_1)
print(type(array_1), end = "\n\n\n")
# Unlike lists, numpy arrays can not have elements of different data types, thus all elements are converted to strings. 



# If we want we can specify what data type should be allowed for creating array

array_1 = np.array([1, 2.5, '3'], dtype = int)
print(array_1)
print(type(array_1), end = "\n\n\n")

array_1 = np.array([1, 2.5, '3'], dtype = float)
print(array_1)
print(type(array_1), end = "\n\n\n")




# We can repeat the list too

array_1 = np.array([1, 2.5, '3'] * 3, dtype = int)
print(array_1)
print(type(array_1), end = "\n\n\n")