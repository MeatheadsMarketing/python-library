import numpy as np
from scipy.optimize import minimize

def gradient_descent(func, x0):
    return minimize(func, x0, method='BFGS')

def newtons_method(f, df, x0, tol=1e-5):
    while abs(f(x0)) > tol:
        x0 = x0 - f(x0)/df(x0)
    return x0
