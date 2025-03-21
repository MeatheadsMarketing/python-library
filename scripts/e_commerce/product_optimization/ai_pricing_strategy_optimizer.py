import openai
import pandas as pd
import numpy as np

def optimize_pricing(product_name, competitor_prices, demand_trend, cost_price):
    """
    AI-powered pricing strategy optimizer that determines the best selling price based on
    competitor prices, demand trends, and cost price.
    """
    avg_competitor_price = np.mean(competitor_prices)
    min_competitor_price = np.min(competitor_prices)
    max_competitor_price = np.max(competitor_prices)

    prompt = (
        f"The average competitor price for {product_name} is ${avg_competitor_price:.2f}. "
        f"The minimum price is ${min_competitor_price:.2f}, and the maximum price is ${max_competitor_price:.2f}. "
        f"The market demand trend is at {demand_trend}/100. "
        f"Given a cost price of ${cost_price:.2f}, suggest an optimal selling price."
    )

    client = openai.OpenAI()

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant specializing in e-commerce pricing optimization."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

# Example Usage
if __name__ == "__main__":
    product_name = "Wireless Noise-Canceling Headphones"
    competitor_prices = [99.99, 129.99, 119.99, 109.99]
    demand_trend = 85
    cost_price = 60.00

    optimal_price = optimize_pricing(product_name, competitor_prices, demand_trend, cost_price)
    print(f"💰 AI-Optimized Price for {product_name}: {optimal_price}")
