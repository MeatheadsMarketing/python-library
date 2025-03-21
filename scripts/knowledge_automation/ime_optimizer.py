
import openai
import os

# Ensure API Key is Set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OpenAI API Key is missing. Set it before running this script.")

def extract_high_impact_insights(text):
    """Extracts deep, high-impact insights from raw scripts or course content."""
    prompt = f"Break down this content into structured, high-impact insights:\n\n{text}"

    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    sample_text = "This module covers advanced SEO techniques and link-building strategies."
    insights = extract_high_impact_insights(sample_text)
    print(f"📌 IME Optimized Insights:\n{insights}")
