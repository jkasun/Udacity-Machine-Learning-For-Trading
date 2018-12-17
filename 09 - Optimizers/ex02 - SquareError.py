import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

"""
    Calculating the square error

    f(x) = mx + c
    line[0] = m
    line[1] = c
"""
def error(line, data):
    err = np.sum((data[:, 1] - (line[0] * data[:, 0] + line[1])) ** 2)
    return err


def fitline(data, error_func):
    """
    Fit a line to given data, using a supplied error function.

    Paramters
    --------------------
    data: 2D array where each row is a point (X0, Y)
    error_func: function that computes the error between a line and observed data

    Returns line that minimizes the error function
    """
    # Generate initial guess for line model
    # slope = 0, intercept = mean of y values
    l = np.float32([0, np.mean(data[:, 1])])

    # Plot the initial guess
    x_ends = np.float32([-5, 5])
    plt.plot(x_ends, l[0] * x_ends + l[1], 'm--',
             linewidth=2.0, label='Initial Guess')

    result = spo.minimize(
        error_func, l, 
        args=(data,), 
        method='SLSQP'
    )

    return result.x


# Define original line
l_orig = np.float32([4, 2])
print("Original line: C0 = {}, C1 = {}".format(l_orig[0], l_orig[1]))
Xorig = np.linspace(0, 10, 21)
Yorig = l_orig[0] * Xorig + l_orig[1]
plt.plot(Xorig, Yorig, 'b--', linewidth=2.0, label="Original line")

# Generate noisy data points
noise_sigma = 3.0
noise = np.random.normal(0, noise_sigma, Yorig.shape)
data = np.asarray([Xorig, Yorig + noise]).T
plt.plot(data[:, 0], data[:, 1], 'go', label="Data Points")

fittedLine = fitline(data, error)
Xfitted = np.linspace(0, 10, 21)
Yfitted = fittedLine[0] * Xfitted + fittedLine[1]
plt.plot(Xfitted, Yfitted, 'r--', linewidth=2.0, label="Fitted Line")

plt.show()
