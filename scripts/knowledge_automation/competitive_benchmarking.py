
import openai
import os

# Ensure API Key is Set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OpenAI API Key is missing. Set it before running this script.")

def generate_competitive_benchmarking(category):
    """Generates competitive analysis insights for an HVHE category."""
    prompt = f"Provide competitive insights for:\n\n{category}\n\nInclude:\n- 🔹 Top Competitors\n- 🔹 Industry Best Practices\n- 🔹 Current Tools Used\n- 🔹 Market Trends\n- 🔹 Expert Insights"

    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    category = "SEO Link-Building Strategies"
    benchmarking = generate_competitive_benchmarking(category)
    print(f"📌 Competitive Benchmarking:\n{benchmarking}")
