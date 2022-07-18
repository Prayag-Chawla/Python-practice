import numpy as np

x = np.random.randint(1, 10, (3,2))
y = np.random.randint(1, 10, (2,3))


print(x, end = "\n\n")
print(y, end = "\n\n")

y = np.transpose(y)
print(y, end = "\n\n")

print(x + y, end = "\n\n")