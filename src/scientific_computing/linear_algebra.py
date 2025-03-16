import numpy as np

def matrix_multiplication(A, B):
    return np.dot(A, B)

def eigenvalues_and_eigenvectors(A):
    return np.linalg.eig(A)

def solve_linear_equation(A, b):
    return np.linalg.solve(A, b)

def singular_value_decomposition(A):
    return np.linalg.svd(A)
