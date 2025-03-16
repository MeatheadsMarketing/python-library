import time
import numpy as np

def track_execution(func, *args):
    start_time = time.time()
    result = func(*args)
    execution_time = time.time() - start_time
    print(f"✅ {func.__name__} executed in {execution_time:.6f} seconds")
    return result, execution_time

def basic_arithmetic(a, b):
    return np.add(a, b), np.subtract(a, b), np.multiply(a, b), np.divide(a, b)

def logarithm_and_exponential(x):
    return np.log(x), np.exp(x)

def factorial(n):
    return np.math.factorial(n)

if __name__ == "__main__":
    log_data = []
    log_data.append(("basic_arithmetic", *track_execution(basic_arithmetic, 10, 5)))
    log_data.append(("logarithm_and_exponential", *track_execution(logarithm_and_exponential, 10)))
    log_data.append(("factorial", *track_execution(factorial, 5)))

    # Save function execution times to CSV
    import csv
    with open("/content/drive/MyDrive/Execution_Results/function_benchmarks.csv", "a", newline="") as f:
        writer = csv.writer(f)
        for log in log_data:
            writer.writerow(log)
