import numpy as np

a = np.random.rand(5, 4)
print(a)

element = a[3,2]
print(element)

# ELements in defined range
slice1 = a[0, 1:3]
print(slice1)

slice2 = a[0:2, 0:2]
print(slice2)

# Step slicing
step = 2
step_slice = a[:, 0:3:step]
print(step_slice)