import requests
from os import getenv
from dotenv import load_dotenv
from typing import Dict, List
import random

# Load environment variables from .env file
load_dotenv()


class UserInteraction:
    """
    Handles detailed user interactions with a simulated search engine, such as querying, clicking on results,
    and determining stopping conditions based on user profiles and current session context.
    """

    def __init__(self, user_profile):
        self.user_profile = user_profile
        self.search_history = []

    def formulate_query(self) -> str:
        """
        Generate a query based on user interests and previous search history.
        """
        interests = self.user_profile.attributes['interests']
        if self.search_history:
            last_query = self.search_history[-1]['query']
            
            query = f"{last_query} updated"
        else:
            
            query = f"Information about {', '.join(interests)}"
        
        return query

    def assess_results(self, search_results: List[str]) -> str:
        """
        Decide which search result to click based on relevance and user's clicking behavior.
        """
        click_preference = self.user_profile.attributes['clickstream_data']
        if click_preference == 'direct_hits':
            # Assume the first result is the most relevant
            chosen_result = search_results[0]
        else:
            # Random or more complex selection logic could be implemented here
            chosen_result = random.choice(search_results)

        return chosen_result

    def decide_stopping(self, session_length: int) -> bool:
        """
        Determine whether to stop searching based on the user's temporal pattern and session length.
        """
        temporal_pattern = self.user_profile.attributes['temporal_patterns']
        if temporal_pattern == 'short' and session_length >= 2:
            return True
        elif temporal_pattern == 'medium' and session_length >= 5:
            return True
        elif temporal_pattern == 'long' and session_length >= 10:
            return True
        return False

    def handle_search_interaction(self, search_engine) -> List[Dict]:
        """
        Conduct an entire search interaction sequence for one session.
        """
        session_interactions = []
        while True:
            query = self.formulate_query()
            search_results = search_engine.search(query)
            chosen_result = self.assess_results(search_results)
            self.search_history.append({'query': query, 'result': chosen_result})

            session_interactions.append({'query': query, 'clicked': chosen_result})
            
            if self.decide_stopping(len(session_interactions)):
                break
        
        return session_interactions

class BingSearchEngine:
    """
    A class to interact with Microsoft Bing's Search API.
    """
    def __init__(self):
        self.api_key = getenv("BING_API_KEY")
        self.base_url = "https://api.bing.microsoft.com/v7.0/search"

    def search(self, query: str) -> List[str]:
        """
        Perform a search query using Bing's Search API and return the top 10 results.
        """
        headers = {"Ocp-Apim-Subscription-Key": self.api_key}
        params = {
            "q": query,
            "count": 10,  # Number of search results to return
            "responseFilter": "Webpages"  # Filter for web page results only
        }
        response = requests.get(self.base_url, headers=headers, params=params)
        response.raise_for_status()  # Raises an exception for HTTP errors
        search_results = response.json()

        # Extract the title or snippet from the search results
        return [result['name'] + ": " + result['snippet'] for result in search_results['webPages']['value']]

def main():
    from profiles import UserProfile  

    user_profile = UserProfile("test_user")
    user_profile.build_profile()

    search_engine = BingSearchEngine()

    # Initialize the user interaction module
    interaction = UserInteraction(user_profile)

    # Run a search interaction session
    results = interaction.handle_search_interaction(search_engine)
    print("Search Session Results:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
