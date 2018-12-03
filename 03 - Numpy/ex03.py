import numpy as np

np.random.seed(693) # seed the random number gen - will generate same random numbers
a = np.random.randint(0, 10, size=(5, 4))

# Total of all elements
print(a.sum())

# Iterate over rows, to compute sum of each col
print ("Sum of each column:\n", a.sum(axis=0))

# Iterate over col, to compute sum of each row
print("Sum of each rows\n", a.sum(axis=1))

# Statistics: min, max, mean (across rows, cols, and overall)
print ("Max of each col\n", a.max(axis=0))
print ("Min of each row\n", a.min(axis=1))
print ("Mean of all elements\n", a.mean())