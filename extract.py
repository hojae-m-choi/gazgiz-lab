import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    try:
        # Send an HTTP request to the URL
        response = requests.get(url)
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all text from the body of the webpage
        text = soup.get_text(separator=' ', strip=True)
        return text
    except requests.RequestException as e:
        return str(e)

# Example URL (replace with your specific URL)
# url = "https://www.example.com"
# text = extract_text_from_url(url)
# print(text)
