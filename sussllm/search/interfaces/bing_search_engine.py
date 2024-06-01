from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import json

# Load environment variables
load_dotenv()

class BingSearchEngine:
    def __init__(self):
        self.api_key = os.getenv('BING_API_KEY')
        self.base_url = "https://api.bing.microsoft.com/v7.0/search"

    def search(self, query):
        headers = {"Ocp-Apim-Subscription-Key": self.api_key}
        params = {"q": query, "textDecorations": True, "textFormat": "HTML"}
        response = requests.get(self.base_url, headers=headers, params=params)
        return response.json()

    def get_curated_content(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract text content from the main content, stripping out all HTML tags
        main_content = soup.find('main')
        if main_content:
            return main_content.get_text(strip=True)
        else:
            return "Main content not found or not identifiable."

def get_serp_json(query):
    bing = BingSearchEngine()
    serp_results = bing.search(query)
    formatted_results = []
    for result in serp_results.get('webPages', {}).get('value', []):
        formatted_results.append({
            "rank": result.get('id'),
            "url": result.get('url'),
            "title": result.get('name'),
            "snippet": result.get('snippet')
        })
    return json.dumps(formatted_results, indent=4)

def get_curated_html_content(url):
    bing = BingSearchEngine()
    curated_content = bing.get_curated_content(url)
    return curated_content


if __name__ == "__main__":
    query = "bollywood growth"
    print(get_serp_json(query))
    url = "http://www.macnn.com/news/"
    print(get_curated_html_content(url))