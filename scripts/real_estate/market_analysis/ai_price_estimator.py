import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def predict_home_price(features, target):
    """Predicts home price using a linear regression model."""
    model = LinearRegression()
    model.fit(features, target)
    return model

# Example usage
if __name__ == "__main__":
    df = pd.read_csv("real_estate_data.csv")
    X = df[["sqft", "bedrooms", "bathrooms"]]
    y = df["price"]
    model = predict_home_price(X, y)
    print(f"✅ Model trained: {model.coef_}")
