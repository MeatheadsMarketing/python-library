
import openai
import os

def encrypt_sensitive_data(data):
    """
    AI-Powered Data Encryption Assistant.
    Encrypts sensitive information using AI-powered encryption techniques.
    """
    prompt = f"Encrypt the following sensitive data using the best encryption method:\n{data}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI encryption expert."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    sensitive_data = "User Password: 12345, Bank Account: 987654321"
    encrypted_info = encrypt_sensitive_data(sensitive_data)
    print(f"🔒 AI-Encrypted Data: {encrypted_info}")
