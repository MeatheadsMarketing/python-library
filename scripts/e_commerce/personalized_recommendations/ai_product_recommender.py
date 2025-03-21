import openai
import os

def recommend_products(user_preferences, browsing_history, purchase_history):
    """
    Generates AI-powered product recommendations based on user preferences, browsing history, and purchase history.
    :param user_preferences: List of preferred product features or categories
    :param browsing_history: List of recently viewed products
    :param purchase_history: List of previously purchased products
    :return: AI-generated recommended products
    """

    prompt = f"Based on the user's preferences {user_preferences}, browsing history {browsing_history}, and purchase history {purchase_history}, generate 5 highly relevant product recommendations."

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant specializing in personalized product recommendations."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    user_preferences = ["Wireless", "Noise-Canceling", "Bluetooth"]
    browsing_history = ["Sony WH-1000XM4", "Bose QuietComfort 45"]
    purchase_history = ["AirPods Pro", "JBL Tune 750"]

    recommendations = recommend_products(user_preferences, browsing_history, purchase_history)
    print(f"🛍️ AI-Powered Product Recommendations:\n{recommendations}")
