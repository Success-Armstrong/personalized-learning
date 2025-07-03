# student_simulator.py

from rl_agent import QLearningAgent
import environment
import random

def train_agent(episodes=500):
    agent = QLearningAgent()
    all_states = environment.get_all_states()

    for _ in range(episodes):
        # Start each episode with a random state
        state = random.choice(all_states)

        for _ in range(10):  # simulate steps per episode
            action = agent.choose_action(state)
            reward = environment.simulate_student_response(state, action)
            next_state = random.choice(all_states)  # move to random next state
            agent.update_q_value(state, action, reward, next_state)
            state = next_state

    return agent
