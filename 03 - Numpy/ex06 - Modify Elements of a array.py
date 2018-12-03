import numpy as np

a = np.random.rand(5, 4)
print(a)

# Asign single value
a[0, 0] = 1
print(a)

# Assign a single value for an entier row
a[0,:] = 2
print(a)

# Modify a col with custom values
a[:, 3] = [1, 2, 3, 4, 5]
print(a)