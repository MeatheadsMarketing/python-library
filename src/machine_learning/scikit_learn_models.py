from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier

def train_linear_regression(X, y):
    """Trains a simple linear regression model."""
    model = LinearRegression()
    model.fit(X, y)
    return model

def train_random_forest(X, y):
    """Trains a Random Forest classifier."""
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    return model
