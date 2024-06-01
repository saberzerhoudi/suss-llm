import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from sussllm.profiles import UserProfile
from sussllm.simulation import SimulationEngine
from sussllm.interaction import UserInteraction
from sussllm.reasoning import ReasoningEngine
from sussllm.utils.logger import setup_logger

def main():
    logger = setup_logger('simulation_logger', 'simulation.log')

    profiles = [UserProfile(str(i)) for i in range(5)]  
    for profile in profiles:
        profile.build_profile()

    simulation_engine = SimulationEngine(profiles)
    sessions = simulation_engine.run_simulation()


    for session in sessions:
        logger.info(f'Session: {session}')

    reasoning_engine = ReasoningEngine()
    for session in sessions:
        context = ' '.join([f'Query: {interaction["query"]["query"]}, Click: {interaction["click"]["clicked"]}' for interaction in session])
        reasoning = reasoning_engine.generate_reasoning(context)
        action = reasoning_engine.decide_next_action(reasoning)
        logger.info(f'Reasoning: {reasoning}, Decided Action: {action}')

if __name__ == "__main__":
    main()
