import requests

def fetch_data_from_api(url):
    """Fetches JSON data from an API"""
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

# Example usage
if __name__ == "__main__":
    data = fetch_data_from_api("https://api.github.com")
    print(data)
