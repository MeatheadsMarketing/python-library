
import openai
import os

def generate_quiz_questions(topic):
    """
    Generates quiz questions and practical tasks for mastery evaluation.
    """
    prompt = f"Create 5 quiz questions and 3 practical application exercises to test knowledge on '{topic}'."

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert knowledge evaluator."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    subject = "Machine Learning Fundamentals"
    evaluation = generate_quiz_questions(subject)
    print(f"📚 Knowledge Evaluation:\n{evaluation}")
