import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def f(x):
    y = (x - 1.5) ** 2 + 0.5
    return y

# Finding the minium value for f(x) = y = (x - 1.5) ** 2 + 0.5
xGuess = 2.0
min_result = spo.minimize(f, xGuess, method='SLSQP', options={'disp': True})
print("Minimal fount at")
print("x = {}, y = {}".format(min_result.x, min_result.fun))

# Plot
Xplot = np.linspace(0.5, 2.5, 21)
Yplot = f(Xplot)
plt.plot(Xplot, Yplot)
plt.plot(min_result.x, min_result.fun, 'ro')
plt.show()