import numpy as np
import scipy.optimize as opt
from numba import jit

@jit(nopython=True)
def fast_sum(arr):
    """Optimized summation using Numba JIT."""
    total = 0
    for x in arr:
        total += x
    return total

def gradient_descent(func, x0):
    """Finds the minimum of a function using gradient descent."""
    result = opt.minimize(func, x0, method='BFGS')
    return result.x, result.fun
