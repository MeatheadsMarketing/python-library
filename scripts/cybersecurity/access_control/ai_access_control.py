
import openai
import os

def analyze_access_policies(access_policies):
    """
    AI-Powered Access Control Manager.
    Evaluates access policies and recommends security improvements.
    """
    prompt = f"Analyze the following access control policies and recommend security improvements:\n{access_policies}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI expert in access control management."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    access_policies = "Policy: User admin access granted to all employees. MFA disabled."
    security_review = analyze_access_policies(access_policies)
    print(f"🛡️ AI Access Control Review: {security_review}")
