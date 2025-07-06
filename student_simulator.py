# student_simulator.py

from rl_agent import QLearningAgent
import environment
import random

def train_agent(episodes=500):
    actions = ["Watch Video", "Practice Quiz", "Read Theory"]
    agent = QLearningAgent(actions)
    all_states = environment.get_all_states()

    for _ in range(episodes):
        state = random.choice(all_states)
        for _ in range(10):  # steps per episode
            action = agent.choose_action(state)
            reward = environment.simulate_student_response(state, action)
            next_state = random.choice(all_states)
            agent.update_q_value(state, action, reward, next_state)
            state = next_state

    return agent
