

import openai
import os

def rewrite_article(article):
    """Rewrites an article while maintaining the original meaning."""
    prompt = f"Rewrite the following article in a fresh and engaging way while keeping the meaning intact:\n\n{article}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert article rewriter."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    article = "Artificial intelligence is shaping the future by enabling smarter automation, predictive analytics, and enhanced decision-making."
    rewritten_article = rewrite_article(article)
    print(f"📝 AI-Rewritten Article:\n\n{rewritten_article}")
