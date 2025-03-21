import openai

def generate_product_description(product_name, features):
    """
    Generates an AI-powered product description based on product name and key features.
    """
    prompt = f"Write an engaging and SEO-optimized product description for {product_name} with features: {', '.join(features)}."
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message["content"]

# Example usage
if __name__ == "__main__":
    product_name = "Wireless Noise-Canceling Headphones"
    features = ["Bluetooth 5.0", "30-hour battery life", "Active noise canceling", "Built-in microphone"]
    
    description = generate_product_description(product_name, features)
    print(f"🛍️ AI-Generated Product Description:\n\n{description}")
