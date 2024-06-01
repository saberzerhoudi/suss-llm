import json

class PromptManager:
    def __init__(self, template_file=None):
        self.templates = {
            "query_behavior": """
You are a search engine user with your own profile. Your task is to interact with search engines {max_exceeds_times} times. You have two types of operations to perform:
- Search[query]: When the current round has not reached {max_exceeds_times} times, please raise the next question based on your profile and web browsing history. Your query should be an entity phrase that has a similar topic to an attribute in your user profile. The query must be concise and clear. For example, Search[bollywood growth], Search[junk food tracks], Search[pseudocyesis information], Search[location of port arthur].
- Finish[finish], When the current round exceeds {max_exceeds_times} times, you need to end your interaction with search engines. For example, Finish[Finish]
** Your Profile ** {profile}
** Web browsing (click) history ** {scratchpad}
** Your action **
""",
            "click_behavior": """
You are a search engine user with your own profile. Your task is to click on the most relevant page.
In this interaction, you raised the question of **query**. You have received several webpage titles returned by the search engine.
Now, based on your profile, web browsing history, and the relevance between the query and the titles, please choose the most relevant webpage to click on. Please note that you can only output one number from 1 to 10 to represent the title you are about to click on, and cannot output any other content.
** Your Profile ** {profile}
** Web browsing (click) history ** {scratchpad}
** Query ** {query}
** Titles ** {titles}
** Your click **
"""
        }
        if template_file:
            with open(template_file, 'r') as file:
                self.templates = json.load(file)

    def get_prompt(self, prompt_type, **kwargs):
        prompt_template = self.templates[prompt_type]
        return prompt_template.format(**kwargs)


if __name__ == "__main__":
    prompt_manager = PromptManager()


    user_profile = "User Profile: Interests in technology, health, and entertainment"
    scratchpad = "Previous clicks: Tech article, Health news"
    query = "What are the latest advancements in AI?"
    titles = "1. AI breakthrough 2. AI in healthcare 3. AI for entertainment"

    query_prompt = prompt_manager.get_prompt("query_behavior", max_exceeds_times=5, profile=user_profile, scratchpad=scratchpad)
    click_prompt = prompt_manager.get_prompt("click_behavior", profile=user_profile, scratchpad=scratchpad, query=query, titles=titles)

    print(query_prompt)
    print(click_prompt)
