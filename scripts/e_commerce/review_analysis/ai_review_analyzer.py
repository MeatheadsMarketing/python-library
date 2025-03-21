
import openai
import os

# Set OpenAI API Key Securely
# Replace 'your-secret-api-key' with your actual OpenAI API key
os.environ["OPENAI_API_KEY"] = "your-secret-api-key" 

# Function to Analyze Product Reviews
def analyze_reviews(product_name, reviews):
    """
    AI-powered sentiment analysis of customer reviews.
    
    :param product_name: Name of the product
    :param reviews: List of customer reviews
    :return: Summarized sentiment and insights
    """
    prompt = f"Analyze the following reviews for {product_name}. Provide sentiment analysis (positive, neutral, or negative) and key insights:\n\n"
    prompt += "\n".join(reviews)

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant specializing in sentiment analysis for e-commerce product reviews."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    product = "Wireless Earbuds"
    sample_reviews = [
        "Amazing sound quality and battery life!",
        "The fit is a bit uncomfortable for long hours.",
        "Connectivity issues with my phone.",
        "Best purchase ever! Highly recommend.",
        "Noise cancellation is not as expected, but good for the price."
    ]

    insights = analyze_reviews(product, sample_reviews)
    print(f"🛒 AI-Generated Sentiment Analysis for {product}:\n\n{insights}")
