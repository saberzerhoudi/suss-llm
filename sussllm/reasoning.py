import openai
from dotenv import load_dotenv
from os import getenv

# Load environment variables
load_dotenv()

class ReasoningEngine:
    """
    A class to integrate large language models for reasoning and decision-making in simulated user search sessions.
    """
    def __init__(self):
        self.api_key = getenv("OPENAI_API_KEY")
        self.engine_id = 'gpt-3.5-turbo-0125'  

    def generate_reasoning(self, context: str) -> str:
        """
        Use an LLM to generate reasoning based on the given context.
        """
        try:
            response = openai.Completion.create(
                engine=self.engine_id,
                prompt=context,
                max_tokens=4000,
                n=1,
                stop=None,
                temperature=0
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Error in generating reasoning: {str(e)}")
            return ""

    def decide_next_action(self, reasoning: str) -> str:
        """
        Determine the next action (e.g., new query, refine search, stop searching) based on the LLM's reasoning.
        """
        if "refine search" in reasoning.lower():
            return "refine_search"
        elif "stop searching" in reasoning.lower():
            return "stop_search"
        else:
            return "continue_search"

def main():
  
    context = "The user searched for 'climate change effects' but found results too general."
    reasoning_engine = ReasoningEngine()

    reasoning = reasoning_engine.generate_reasoning(context)
    print(f"Generated Reasoning: {reasoning}")

    action = reasoning_engine.decide_next_action(reasoning)
    print(f"Decided Action: {action}")

if __name__ == "__main__":
    main()
