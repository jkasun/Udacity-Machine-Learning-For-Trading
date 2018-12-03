import numpy as np

# Empty array - with initial random memory value
# print(np.empty(5))
# print(np.empty((5, 4, 3)))

# Creating array full of once
# print(np.ones((5, 4)))

# Defining data type
int_array = np.ones((5, 4), dtype=np.int_)
# print(int_array)

# Generating random value
random_arry = np.random.random((5, 4))
# print(random_arry)

# With rand method
r_arr_t2 = np.random.rand(5, 4)
# print(r_arr_t2)

# Sample numbers from a Gaussian (normal) distribution
r_gaussian = np.random.normal(size=(2, 3)) # 'standard normal' (mean = 0, s.d = 1)
# print(r_gaussian)

r_gaussian_2 = np.random.normal(50, 10, size=(2, 3)) # change mean to 50 and sd to 10
# print(r_gaussian_2)

# Random Integers
np.random.randint(10) # a single integer in [0, 10)
np.random.randint(0, 10) # same as aboce [low, high)
np.random.randint(0, 10, size=5) # 5 random integers 1d array
r_sample = np.random.randint(0, 10, size=(2,3)) # 2x3 array of random integers

# Get shape of the arry
print(r_sample.shape)

# Size of the array - All elements
print(r_sample.size)

# Get data type of the array
print(r_sample.dtype)