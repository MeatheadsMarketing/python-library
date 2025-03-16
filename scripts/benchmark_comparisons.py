import time
import numpy as np
import scipy.optimize
import csv
from src.scientific_computing.numerical_computations import basic_arithmetic
from src.scientific_computing.optimization import gradient_descent

def benchmark_method(method_name, func, *args):
    start_time = time.time()
    result = func(*args)
    execution_time = time.time() - start_time
    return method_name, execution_time

# Benchmark Different Methods
benchmarks = []
benchmarks.append(benchmark_method("NumPy Basic Arithmetic", basic_arithmetic, 10, 5))
benchmarks.append(benchmark_method("SciPy Gradient Descent", gradient_descent, lambda x: x**2, 2.0))

# Save Results
csv_file = "/content/drive/MyDrive/Execution_Results/method_comparisons.csv"
with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Method", "Execution Time (s)"])
    writer.writerows(benchmarks)

print(f"✅ Method comparisons saved in {csv_file}")
