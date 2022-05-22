import numpy as np

##### 2 D Array

two_d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_d, end = "\n\n")


# Indexing
print(two_d[2][1])    # Element present at 2 row 1 column will get printed

# Another method to get the same result is, 
print(two_d[2, 1], end = "\n\n")



# Slicing
print(two_d[1, :2], end = "\n\n")  # This will print elements present at 0 and 1 index position of 1 row

print(two_d[:, :2], end = "\n\n")  # This will print elements present at 0 and 1 index position of all rows

print(two_d[:2, 2], end = "\n\n")    # This will print elements present at 2 column of 0 and 1 rows.

print(two_d[1:3, 1:3])