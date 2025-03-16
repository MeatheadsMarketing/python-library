import dask.dataframe as dd
import pandas as pd

def load_large_dataset(file_path):
    """Loads a large dataset using Dask for scalable processing."""
    df = dd.read_csv(file_path)
    return df.compute()

def optimize_pandas(df):
    """Optimizes Pandas dataframe memory usage."""
    for col in df.select_dtypes(include=["float"]).columns:
        df[col] = pd.to_numeric(df[col], downcast="float")
    return df
