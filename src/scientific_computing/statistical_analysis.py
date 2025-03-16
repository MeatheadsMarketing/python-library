import numpy as np
import scipy.stats as stats

def descriptive_statistics(data):
    return {
        "mean": np.mean(data),
        "median": np.median(data),
        "variance": np.var(data),
        "skewness": stats.skew(data),
        "kurtosis": stats.kurtosis(data)
    }

def hypothesis_testing(sample1, sample2):
    return stats.ttest_ind(sample1, sample2)

def regression_analysis(X, y):
    return np.linalg.lstsq(X, y, rcond=None)
