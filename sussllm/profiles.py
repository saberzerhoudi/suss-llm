import json
from dataclasses import dataclass, field
from typing import Dict, List
import random

# from external_data_processor import fetch_real_user_data
# from gpt_module import generate_gpt_text

@dataclass
class UserProfile:
    user_id: str
    temporal_patterns: str = field(default='')
    search_query_analysis: Dict[str, bool] = field(default_factory=dict)
    clickstream_data: str = field(default='')
    advanced_search_usage: str = field(default='')
    interests: List[str] = field(default_factory=list)
    querying_behavior: str = field(default='')
    snippet_relevance: Dict[str, float] = field(default_factory=dict)
    stopping_rules: str = field(default='')

    def generate_behavioral_profile(self):
        # Define attribute values using hybrid generation techniques
        self.temporal_patterns = random.choice(['short', 'medium', 'long'])
        self.search_query_analysis = {
            'spelling_corrections': random.choice([True, False]),
            'synonym_usage': random.choice([True, False])
        }
        self.clickstream_data = random.choice(['direct_hits', 'iterative_refinement'])
        self.advanced_search_usage = random.choice(['operators', 'filters', 'none'])
        self.interests = random.sample(['technology', 'health', 'education', 'sports', 'entertainment'], k=2)

    def generate_component_profile(self):
        # Simulate detailed user interactions as per the SimIIR framework
        self.querying_behavior = random.choice(['focused', 'exploratory', 'mixed'])
        self.snippet_relevance = {'high': 0.8, 'medium': 0.5, 'low': 0.2}
        self.stopping_rules = random.choice(['satisfaction', 'frustration', 'information_gain'])

    def build_profile(self):
        self.generate_behavioral_profile()
        self.generate_component_profile()

    def to_json(self):
        return json.dumps(self.__dict__, indent=4)


@dataclass
class UserSearchAgent:
    user_id: str
    profile: Dict[str, any]
    state: Dict[str, List[str]] = field(default_factory=dict)

    def update_state(self, key: str, value: str):
        if key in self.state:
            self.state[key].append(value)
        else:
            self.state[key] = [value]

    def generate_query(self):
        query = f"Find information on {self.profile['interests'][0]}"
        self.update_state('queries', query)
        return query

    def select_result(self, results: List[str]):
        return results[0]  

    def decide_next_action(self):
        return "continue_search" if len(self.state.get('queries', [])) < 3 else "stop_search"

def simulate_search_session(agent: UserSearchAgent, search_engine):
    while True:
        query = agent.generate_query()
        results = search_engine.search(query)
        clicked_result = agent.select_result(results)
        agent.update_state('clicks', clicked_result)

        decision = agent.decide_next_action()
        if decision == "stop_search":
            break

    return agent.state


def load_profiles_from_json(json_file: str) -> List[UserProfile]:
    with open(json_file, 'r') as file:
        data = json.load(file)
    return [UserProfile(**user) for user in data]

def save_profiles_to_json(profiles: List[UserProfile], output_file: str):
    with open(output_file, 'w') as file:
        json_data = [json.loads(profile.to_json()) for profile in profiles]
        json.dump(json_data, file, indent=4)

if __name__ == "__main__":

    profiles = [UserProfile(user_id=str(i)) for i in range(5)]
    for profile in profiles:
        profile.build_profile()
        print(profile.to_json())
    save_profiles_to_json(profiles, 'user_profiles.json')
