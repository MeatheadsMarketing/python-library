import dask.array as da
from multiprocessing import Pool

def dask_parallel_sum(arr):
    """Computes the sum of an array using Dask."""
    dask_arr = da.from_array(arr, chunks=1000)
    return dask_arr.sum().compute()

def multiprocessing_sum(arr):
    """Splits the array across CPU cores and sums elements in parallel."""
    with Pool() as pool:
        chunk_size = len(arr) // pool._processes
        result = pool.map(sum, [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)])
    return sum(result)
