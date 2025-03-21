import openai
import os

def predict_demand(product_name, sales_data, market_trend):
    avg_sales = sum(sales_data) / len(sales_data)  # Normalize market trend
    prompt = f"The market trend is at {market_trend}. Predict the expected demand for {product_name}."

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant specializing in demand forecasting."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    product_name = "Wireless Earbuds"
    sales_data = [500, 550, 600, 750, 800]
    market_trend = 0.85

    forecast = predict_demand(product_name, sales_data, market_trend)
    print(f"📈 AI-Predicted Demand for {product_name}: {forecast} units")
