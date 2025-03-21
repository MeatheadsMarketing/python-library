
import openai
import os

# Ensure API Key is Set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OpenAI API Key is missing. Set it before running this script.")

def generate_skill_evaluation(category):
    """Creates a structured skill evaluation test for an HVHE category."""
    prompt = f"Create a skill mastery evaluation for:\n\n{category}\n\nInclude:\n- 🔹 3 Basic-Level Questions\n- 🔹 3 Intermediate-Level Questions\n- 🔹 3 Advanced-Level Questions\n- 🔹 1 Practical Scenario Task"

    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    category = "Technical SEO"
    evaluation = generate_skill_evaluation(category)
    print(f"📌 Skill Evaluation:\n{evaluation}")
