import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """Scrapes text content from a webpage"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text()

# Example usage
if __name__ == "__main__":
    content = scrape_website("https://www.wikipedia.org")
    print(content[:500])  # Preview first 500 characters
