import ray

ray.init(ignore_reinit_error=True)

@ray.remote
def compute_large_dataset(data_chunk):
    """Distributes AI workloads across multiple nodes using Ray."""
    return sum(data_chunk)

def run_distributed_computation(data):
    """Splits dataset and processes it in parallel using Ray."""
    chunk_size = len(data) // 4
    results = ray.get([compute_large_dataset.remote(data[i:i + chunk_size]) for i in range(0, len(data), chunk_size)])
    return sum(results)
