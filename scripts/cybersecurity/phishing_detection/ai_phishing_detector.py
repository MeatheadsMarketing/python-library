
import openai
import os

def detect_phishing(emails):
    """
    AI-Powered Phishing Detection.
    Analyzes emails to detect potential phishing threats.
    """
    prompt = f"Analyze the following emails and detect any potential phishing threats:\n{emails}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI cybersecurity expert specializing in phishing detection."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    sample_emails = "Subject: Urgent! Your bank account needs verification. Click the link: http://suspicious-bank.com"
    alert = detect_phishing(sample_emails)
    print(f"📧 AI Phishing Detection Alert: {alert}")
