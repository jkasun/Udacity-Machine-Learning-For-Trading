import numpy as np

a = np.array([
    (1, 2, 3, 4, 5),
    (10, 20, 30, 40, 50)
], dtype=np.int_)

print(a)

print (a * 2)
print (a / 2)
print (a / 2.0)

b = a * 2

print (a + b)
print (a - b)
print (a * b)
print (a / b)
print (np.matmul(a, b))