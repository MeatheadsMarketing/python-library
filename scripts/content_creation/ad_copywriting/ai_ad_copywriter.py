
import openai
import os

def generate_ad_copy(product, tone="persuasive"):
    """Generates engaging ad copy for a product with a specific tone."""
    prompt = f"Write an {tone} advertisement for {product}."

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert ad copywriter."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    product = "AI-powered marketing automation tool"
    ad_copy = generate_ad_copy(product, "enthusiastic")
    print(f"📢 AI-Generated Ad Copy:\n\n{ad_copy}")
