# rl_agent.py

import numpy as np
import environment
import random


class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.alpha = alpha      # learning rate
        self.gamma = gamma      # discount factor
        self.epsilon = epsilon  # exploration rate

        self.states = environment.get_all_states()
        self.actions = environment.get_possible_actions()

        self.q_table = self._initialize_q_table()

    def _initialize_q_table(self):
        q_table = {}
        for state in self.states:
            q_table[state] = {action: 0.0 for action in self.actions}
        return q_table

    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            return random.choice(self.actions)  # explore
        else:
            # exploit: choose best known action
            return max(self.q_table[state], key=self.q_table[state].get)

    def update_q_value(self, state, action, reward, next_state):
        old_value = self.q_table[state][action]
        next_max = max(self.q_table[next_state].values())

        # Q-learning update rule
        new_value = old_value + self.alpha * (reward + self.gamma * next_max - old_value)
        self.q_table[state][action] = new_value

    def get_q_table(self):
        return self.q_table



import numpy as np

def save_q_table(self, filename="q_table.npy"):
    np.save(filename, self.q_table)

def load_q_table(self, filename="q_table.npy"):
    self.q_table = np.load(filename, allow_pickle=True).item()

