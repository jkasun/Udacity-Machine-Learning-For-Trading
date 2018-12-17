import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def error_poly(C, data):
    """
        Compute error between given polynomial and observed data

        Prameters
        --------------
        C: numpy.poly1d object or equivalent array representing the polynomial coefficients
        data: 2D array where each row is a point (x, y)

        Returns error as a single real value 
    """

    # Metric: Sum of squared y-axis differences
    err = np.sum((data[:, 1] - np.polyval(C, data[:, 0])) ** 2)
    return err


def fit_poly(data, error_func, degree=3):
    """
        Fit a polynomial to given data, using supplied error function

        Parameters
        -----------------
        data: 2D array where each row is a point(x, y)
        error_func: function that computes the error between a polynomial observerd data

        Returns polynomial that minimizes the error function
    """

    # Generate initial guess for polynomial model (all coeffs = 1)
    Cguess = np.poly1d(np.ones(degree + 1, dtype=np.float32))

    # Plot initial guess
    x = np.linspace(-5, 5, 21)
    plt.plot(x, np.polyval(Cguess, x), 'm--', linewidth=2.0, label="Initial Guess")

    # Call optimizer to minimize the error function
    result = spo.minimize(error_func, Cguess, args=(data, ), method='SLSQP')
    return np.poly1d(result.x)

# Define the original poly
c_orig = np.poly1d([1.625, -10.55, -7.031, 64.63, 51.95])
Xorig = np.linspace(-5, 5, 21)
Yorig = c_orig(Xorig)
plt.plot(Xorig, Yorig, 'b--', linewidth=2.0, label="Original Polynomial")

# Generate noisy data points
noise_sigma = 1.0
noise = np.random.normal(0, noise_sigma, Yorig.shape)
data = np.random.normal([Xorig, Yorig + noise]).T
plt.plot(data[:, 0], data[:, 1], 'go', label="Data Points")

# Generating the fitted poly
fittedPoly = fit_poly(data, error_poly, degree=4)
Xfitted = np.linspace(-5, 5, 21)
Yfitted = fittedPoly(Xfitted)
plt.plot(Xfitted, Yfitted, 'r--', linewidth=2.0, label="Fitted Polynomial")

plt.show()


