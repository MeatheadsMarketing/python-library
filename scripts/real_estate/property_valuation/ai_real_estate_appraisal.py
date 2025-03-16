import numpy as np
from sklearn.linear_model import Ridge

def predict_property_value(features, target):
    """Predicts property value using Ridge Regression."""
    model = Ridge(alpha=1.0)
    model.fit(features, target)
    return model

# Example usage
if __name__ == "__main__":
    data = np.array([[2000, 3, 2], [2500, 4, 3], [1800, 2, 1]])
    prices = np.array([500000, 650000, 400000])
    model = predict_property_value(data, prices)
    print(f"✅ Model trained: {model.coef_}")
