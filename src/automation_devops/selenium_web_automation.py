from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def open_google_search(query):
    """Automates a Google search using Selenium."""
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys(query + Keys.RETURN)
