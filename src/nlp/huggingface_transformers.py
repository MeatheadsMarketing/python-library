from transformers import pipeline

def sentiment_analysis(text):
    """Uses a pre-trained Hugging Face model for sentiment analysis."""
    classifier = pipeline("sentiment-analysis")
    return classifier(text)
