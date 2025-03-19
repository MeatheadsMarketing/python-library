import alpaca_trade_api as tradeapi
import yfinance as yf
import datetime
import time

API_KEY = "your-alpaca-api-key"
SECRET_KEY = "your-alpaca-secret-key"
BASE_URL = "https://paper-api.alpaca.markets"

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

def fetch_stock_price(symbol):
    stock = yf.Ticker(symbol)
    return stock.history(period="1d")['Close'].iloc[-1]

def trade(stock_symbol, target_price):
    stock_price = fetch_stock_price(stock_symbol)
    print(f"Current Price of {stock_symbol}: {stock_price}")

    if stock_price < target_price:
        api.submit_order(
            symbol=stock_symbol,
            qty=1,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
        print(f"✅ Bought {stock_symbol} at {stock_price}")
    else:
        print(f"❌ No trade executed for {stock_symbol}")

if __name__ == "__main__":
    trade("AAPL", 150)
