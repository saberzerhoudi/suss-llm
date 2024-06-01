from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()

class GoogleSearchEngine:
    def __init__(self):
        self.api_key = os.getenv('GOOGLE_API_KEY')
        self.cse_id = os.getenv('GOOGLE_CSE_ID')
        self.base_url = "https://www.googleapis.com/customsearch/v1"

    def search(self, query):
        params = {
            "key": self.api_key,
            "cx": self.cse_id,
            "q": query,
        }
        response = requests.get(self.base_url, params=params)
        return response.json()

def get_serp_json(query):
    google = GoogleSearchEngine()
    serp_results = google.search(query)
    formatted_results = []
    for result in serp_results.get('items', []):
        formatted_results.append({
            "rank": result.get('cacheId'),  
            "url": result.get('link'),
            "title": result.get('title'),
            "snippet": result.get('snippet')
        })
    return formatted_results


if __name__ == "__main__":
    query = "bollywood growth"
    serp_results = get_serp_json(query)
    for result in serp_results:
        print(result)