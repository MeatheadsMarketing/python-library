def predict_luxury_buyer_profile(net_worth, investment_portfolio, location_preference):
    """Predicts high-net-worth buyer likelihood for luxury properties."""
    if net_worth > 5_000_000 and investment_portfolio > 2_000_000:
        return f"Highly interested in luxury real estate in {location_preference}"
    return "Not a target luxury buyer"

# Example usage
if __name__ == "__main__":
    prediction = predict_luxury_buyer_profile(10_000_000, 3_000_000, "Beverly Hills")
    print(f"✅ Luxury Buyer Prediction: {prediction}")
