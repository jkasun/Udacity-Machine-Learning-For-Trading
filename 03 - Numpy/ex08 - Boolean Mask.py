import numpy as np

np.random.seed(693) # seed the random number gen - will generate same random numbers
a = np.random.randint(0, 10, size=(5, 4))
print(a)

mean = a.mean()
print("Mean", mean)

# Masking values less than mean
masked1 = a[a > mean]
print(masked1)

# Replace less numbers with mean
a [ a < mean] = mean
print(a)