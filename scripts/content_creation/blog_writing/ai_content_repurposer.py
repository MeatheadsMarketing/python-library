import openai
import os

def repurpose_content(original_text, format="blog"):
    """Repurposes content into different formats like blog posts, LinkedIn articles, or email newsletters."""
    prompt = f"Convert the following content into an engaging {format}:\n\n{original_text}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert in content repurposing."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    original_text = "AI is changing the way businesses operate by automating mundane tasks and optimizing workflows."
    new_format = "LinkedIn article"
    repurposed_content = repurpose_content(original_text, new_format)
    print(f"♻️ AI-Repurposed Content:\n\n{repurposed_content}")
