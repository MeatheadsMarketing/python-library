import numpy as np
from numba import jit, cuda

@jit(nopython=True)
def fast_matrix_multiply(A, B):
    """Performs matrix multiplication using JIT compilation."""
    return np.dot(A, B)

@cuda.jit
def gpu_addition(A, B, C):
    """Performs element-wise addition using GPU."""
    i = cuda.grid(1)
    if i < A.size:
        C[i] = A[i] + B[i]
