
import openai
import os

# Ensure API Key is Set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OpenAI API Key is missing. Set it before running this script.")

def generate_execution_plan(category):
    """Creates a structured execution plan for each HVHE category."""
    prompt = f"Design a full execution blueprint for the category:\n\n{category}\n\nInclude:\n- 🔹 Key Steps\n- 🔹 Required Tools\n- 🔹 Metrics for Validation\n- 🔹 Optional Automations"

    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    category = "SEO Optimization Strategy"
    blueprint = generate_execution_plan(category)
    print(f"📌 Execution Plan:\n{blueprint}")
