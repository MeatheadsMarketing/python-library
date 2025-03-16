import openai
import os

# Load OpenAI API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_ai_response(prompt):
    """Generates AI responses using OpenAI's GPT API"""
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Example usage
if __name__ == "__main__":
    print(generate_ai_response("What is the future of AI?"))
