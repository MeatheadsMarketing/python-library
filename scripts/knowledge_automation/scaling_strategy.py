
import openai
import os

# Ensure API Key is Set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OpenAI API Key is missing. Set it before running this script.")

def generate_scaling_strategy(category):
    """Provides a scaling strategy to apply the knowledge from an HVHE category."""
    prompt = f"Suggest a strategy to scale and apply the insights from:\n\n{category}\n\nInclude:\n- 🔹 Reuse in Other Courses\n- 🔹 Client Work Use Cases\n- 🔹 Portfolio Project Applications\n- 🔹 Automation Opportunities"

    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    category = "Technical SEO Mastery"
    strategy = generate_scaling_strategy(category)
    print(f"📌 Scaling Strategy:\n{strategy}")
