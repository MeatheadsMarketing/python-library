import numpy as np
import yfinance as yf

def calculate_var(stock_symbol, confidence_level=95):
    stock = yf.Ticker(stock_symbol)
    df = stock.history(period="1y")["Close"]
    
    daily_returns = df.pct_change().dropna()
    percentile = np.percentile(daily_returns, 100 - confidence_level)
    
    var = percentile * df.iloc[-1]
    return round(var, 2)

if __name__ == "__main__":
    stock = "AAPL"
    risk = calculate_var(stock)
    print(f"📉 Estimated Value at Risk (VaR) for {stock}: ${risk}")
