import alpaca_trade_api as tradeapi
import requests
import pandas as pd
import ta  # Technical indicators library
from transformers import pipeline
import schedule
import time
import os
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import alpaca_trade_api as tradeapi
import requests
import pandas as pd
import ta  # Technical indicators library
from alpha_vantage.timeseries import TimeSeries
from transformers import pipeline
import schedule
import time
import os

# 🚀 Load API credentials from environment variables
# 🚀 Alpha Vantage API Key (Replace with your actual key)
ALPHA_VANTAGE_API_KEY = "W0D0AH513XHN2JN3"
# 🚀 Load Alpaca API credentials from environment variables (More secure!)
API_KEY = "PKAOTVXQ0B5G8S2EVBHA"
API_SECRET = "rMOfwCjSDYo1gBcEfKqCqhjM6Lzlr8dwNyPhePue"
BASE_URL = "https://paper-api.alpaca.markets"

# 🚀 Connect to Alpaca API
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version="v2")

# 🚀 Function to Fetch Stock Data from Alpha Vantage
def get_stock_data(symbol):
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format="pandas")
    data, meta_data = ts.get_daily(symbol=symbol, outputsize="compact")
    return data

# 🚀 Fetch and Display AAPL Stock Data
df = get_stock_data("AAPL")
print("📊 Latest Stock Data for AAPL:\n", df.head())

# 🚀 Compute Moving Averages
df["SMA_20"] = ta.trend.sma_indicator(df["4. close"], window=20)
df["SMA_50"] = ta.trend.sma_indicator(df["4. close"], window=50)

# 🚀 Trading strategy: Buy if 20-day SMA crosses above 50-day SMA
if df["SMA_20"].iloc[-1] > df["SMA_50"].iloc[-1]:  
    api.submit_order(symbol="AAPL", qty=1, side="buy", type="market", time_in_force="gtc")
    print("📈 Buy Signal: Bought 1 share of AAPL!")
else:
    print("🔴 No Buy Signal - Waiting for SMA Crossover")

# 🚀 Load FinBERT sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")
news = "Apple stock is surging after a strong earnings report!"
sentiment = sentiment_pipeline(news)

# 🚀 Trading decision based on sentiment analysis
if sentiment[0]["label"] == "POSITIVE":
    api.submit_order(symbol="AAPL", qty=1, side="buy", type="market", time_in_force="gtc")
    print("✅ AI Sentiment Positive: Bought 1 share of AAPL!")
else:
    print("🔴 AI Sentiment Negative - No trade executed")

# 🚀 Automate Daily Execution
def run_bot():
    print("🚀 Running Trading Bot...")
    os.system("python app.py")

schedule.every().day.at("09:30").do(run_bot)
while True:
    schedule.run_pending()
    time.sleep(60)
