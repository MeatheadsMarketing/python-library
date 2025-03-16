import numpy as np
import scipy.special as sp

def basic_arithmetic(a, b):
    """Performs addition, subtraction, multiplication, and division."""
    return np.add(a, b), np.subtract(a, b), np.multiply(a, b), np.divide(a, b)

def logarithm_exponential(x):
    """Computes log, exp, and factorial functions."""
    return np.log(x), np.exp(x), sp.factorial(x)

def complex_operations(a, b):
    """Performs addition and multiplication of complex numbers."""
    return np.add(complex(a), complex(b)), np.multiply(complex(a), complex(b))
