import os
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import openai

def optimize_portfolio(portfolio):
    """Optimizes portfolio allocation based on risk-return tradeoff."""
    prompt = f"Optimize the following investment portfolio: {portfolio}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI financial advisor optimizing portfolio allocations."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example usage
if __name__ == "__main__":
    portfolio = {"stocks": {"AAPL": 40, "GOOGL": 30, "AMZN": 30}, "bonds": 20, "cash": 10}
    optimized_portfolio = optimize_portfolio(portfolio)
    print(f"📈 AI Portfolio Optimization: {optimized_portfolio}")
