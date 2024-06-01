import random
import time
from profiles import UserProfile, load_profiles_from_json
from typing import List, Dict, Any

class SimulationEngine:
    """
    Manages the simulation environment where user profiles interact with a simulated search engine.
    """
    def __init__(self, user_profiles: List[UserProfile]):
        self.user_profiles = user_profiles
        self.search_sessions = []

    def simulate_query(self, user_profile: UserProfile) -> Dict[str, Any]:
        """
        Simulate a query based on the user's search pattern attributes.
        """
        interests = user_profile.attributes['interests']
        query_patterns = user_profile.attributes['search_query_patterns']
        query = f"Search for {' or '.join(interests)}"

        if query_patterns['corrections']:
            query += " with correct spelling"
        if query_patterns['synonym_usage']:
            query = query.replace('Search', 'Find')

        return {'query': query, 'timestamp': time.time()}

    def simulate_click(self, user_profile: UserProfile, search_results: List[str]) -> Dict[str, Any]:
        """
        Simulate a user click based on the attractiveness of search results and user's clickstream patterns.
        """
        if user_profile.attributes['clickstream_data'] == 'direct_hits':
            clicked = search_results[0] 
        else:
            clicked = random.choice(search_results) 

        return {'clicked': clicked, 'timestamp': time.time()}

    def simulate_search_session(self, user_profile: UserProfile) -> List[Dict[str, Any]]:
        """
        Simulates a complete search session for a given user profile.
        """
        session = []
        queries = random.randint(1, 5)  

        for _ in range(queries):
            query = self.simulate_query(user_profile)
            search_results = [f"Result {i+1} for {query['query']}" for i in range(10)]
            click = self.simulate_click(user_profile, search_results)
            
            session.append({'query': query, 'click': click})

            if random.random() < 0.2:  
                break

        return session

    def run_simulation(self):
        """
        Runs the simulation across all provided user profiles.
        """
        for profile in self.user_profiles:
            session = self.simulate_search_session(profile)
            self.search_sessions.append(session)

        return self.search_sessions

def main():
    user_profiles = load_profiles_from_json('user_profiles.json')
    engine = SimulationEngine(user_profiles)

    all_sessions = engine.run_simulation()
    
    for session in all_sessions:
        print(session)

if __name__ == "__main__":
    main()
