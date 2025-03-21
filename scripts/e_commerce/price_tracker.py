
import openai
import os

# ✅ Set up API Key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def track_competitor_prices(product_url):
    prompt = f"Monitor competitor price from {product_url} and report changes."
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Track competitor prices dynamically."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    print(track_competitor_prices("https://example.com/product"))
