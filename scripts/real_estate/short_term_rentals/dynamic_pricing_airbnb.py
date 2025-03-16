def dynamic_airbnb_pricing(night_demand, seasonality_factor):
    """Adjusts short-term rental pricing dynamically."""
    base_price = 100  # Example base price
    adjusted_price = base_price * (1 + night_demand * 0.1) * seasonality_factor
    return adjusted_price

# Example usage
if __name__ == "__main__":
    price = dynamic_airbnb_pricing(8, 1.2)
    print(f"✅ Recommended Airbnb Price: ${price:.2f}")
