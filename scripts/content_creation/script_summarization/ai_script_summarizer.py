import openai
import os

def summarize_text(text):
    """Generates a concise summary of given text."""
    prompt = f"Summarize the following text in a concise and engaging way:\n\n{text}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert at summarizing content."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    text = "Artificial intelligence is revolutionizing industries by automating tasks, enhancing decision-making, and driving innovation..."
    summary = summarize_text(text)
    print(f"📌 AI-Generated Summary:\n\n{summary}")
