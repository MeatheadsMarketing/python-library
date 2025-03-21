
import openai
import os

def generate_assistant_ideas(insight_text):
    """
    Converts insights into potential AI assistant project ideas.
    """
    prompt = f"Based on this insight: '{insight_text}', generate a list of AI assistant ideas with their use cases."

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant idea generator."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    insight = "SEO content optimization requires dynamic updates."
    assistant_ideas = generate_assistant_ideas(insight)
    print(f"🛠️ AI Assistant Ideas:\n{assistant_ideas}")
