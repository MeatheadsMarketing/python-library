import os
import csv

# Define CSV file path
csv_dir = "/content/drive/MyDrive/Execution_Results"
csv_file = os.path.join(csv_dir, "method_comparisons.csv")

# Ensure the directory exists
if not os.path.exists(csv_dir):
    os.makedirs(csv_dir)

# Sample data for testing
benchmarks = [
    ["Method", "Execution Time (s)"],
    ["NumPy Basic Arithmetic", 0.0012],
    ["SciPy Gradient Descent", 0.0231]
]

# Write benchmark data
with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(benchmarks)

print(f"✅ Performance benchmarks saved in {csv_file}")
