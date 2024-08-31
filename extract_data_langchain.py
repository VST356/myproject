import requests
from bs4 import BeautifulSoup
import os

# URL to scrape
url = "https://brainlox.com/courses/category/technical"

def fetch_data_from_url(url):
    # Fetch the webpage content
    response = requests.get(url)
    response.raise_for_status()  # Raise an error if the request failed

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract text (customize as needed based on the page structure)
    extracted_text = soup.get_text()

    return extracted_text

def save_to_file(data, filename='data/courses_data.txt'):
    # Ensure data directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Save the data to a file with UTF-8 encoding
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)

if __name__ == "__main__":
    # Fetch and process the URL content
    data = fetch_data_from_url(url)
    
    # Save the extracted data to a file
    save_to_file(data)
    print(f"Data extracted and saved to 'data/courses_data.txt'")
