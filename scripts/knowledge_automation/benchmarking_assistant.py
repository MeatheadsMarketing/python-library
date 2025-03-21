
import openai
import os

# Ensure API Key is Set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
import openai
import os

def benchmark_against_competitors(topic):
    """
    Compares extracted knowledge with industry benchmarks.
    """
    prompt = f"Provide competitive benchmarking insights for '{topic}', including top tools, expert insights, and key metrics."

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a competitive benchmarking analyst."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    category = "Digital marketing analytics"
    benchmarks = benchmark_against_competitors(category)
