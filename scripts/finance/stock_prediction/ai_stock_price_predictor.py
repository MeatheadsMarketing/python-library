import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fetch_stock_data(ticker, start="2020-01-01", end="2024-01-01"):
    stock = yf.Ticker(ticker)
    df = stock.history(period="1d", start=start, end=end)
    return df[['Close']]

def train_model(df):
    df['Prediction'] = df['Close'].shift(-1)  # Predict next day's price
    X = np.array(df.drop(['Prediction'], axis=1))[:-1]
    y = np.array(df['Prediction'])[:-1]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model, X_test, y_test

if __name__ == "__main__":
    df = fetch_stock_data("AAPL")
    model, X_test, y_test = train_model(df)
    
    predictions = model.predict(X_test)
    
    plt.figure(figsize=(10,5))
    plt.plot(y_test, label="Actual Price")
    plt.plot(predictions, label="Predicted Price", linestyle="dashed")
    plt.legend()
    plt.show()

    print("✅ AI Stock Price Prediction Model Completed!")
