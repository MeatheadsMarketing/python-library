import os
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import openai
import requests

def analyze_crypto_market(crypto_symbol):
    """Analyzes market trends for a given cryptocurrency symbol."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies=usd"
    response = requests.get(url).json()
    current_price = response.get(crypto_symbol, {}).get("usd", "N/A")

    prompt = f"The current price of {crypto_symbol} is ${current_price}. Predict its short-term trend based on historical data."

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a financial AI assistant analyzing cryptocurrency trends."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example usage
if __name__ == "__main__":
    prediction = analyze_crypto_market("bitcoin")
    print(f"📊 AI Crypto Market Analysis: {prediction}")
