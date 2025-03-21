
import openai
import os

# Ensure API Key is Set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OpenAI API Key is missing. Set it before running this script.")

def synthesize_lesson(lesson_text):
    """Summarizes a lesson into structured notes with key insights and actionable takeaways."""
    prompt = f"Summarize this lesson with:\n- 🔹 Core Insight\n- 🔹 Real-World Example\n- 🔹 Key Statistic\n- 🔹 'For Dummies' Summary\n\n{lesson_text}"

    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    sample_lesson = "This lesson covers the importance of backlinking for SEO rankings."
    summary = synthesize_lesson(sample_lesson)
    print(f"📌 Lesson Summary:\n{summary}")
