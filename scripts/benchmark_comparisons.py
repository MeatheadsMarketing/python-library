import os
import csv

# Define CSV file path
csv_dir = os.path.expanduser("~/python-library/logs")
csv_file = os.path.join(csv_dir, "method_comparisons.csv")

print(f"✅ Checking if directory exists: {csv_dir}")

# Ensure the directory exists
if not os.path.exists(csv_dir):
    print("📂 Directory does not exist. Creating now...")
    os.makedirs(csv_dir)
else:
    print("📂 Directory already exists.")

# Sample benchmark data
benchmarks = [
    ["Method", "Execution Time (s)"],
    ["NumPy Basic Arithmetic", 0.0012],
    ["SciPy Gradient Descent", 0.0231]
]

print(f"✅ Writing benchmark data to {csv_file}")

# Write benchmark data
with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(benchmarks)

print(f"✅ Performance benchmarks saved in {csv_file}")
