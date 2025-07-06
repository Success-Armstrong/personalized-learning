import os
import numpy as np
import random

class QLearningAgent:
    def __init__(self, actions, learning_rate=0.1, discount_factor=0.9, epsilon=0.2):
        self.actions = actions
        self.q_table = {}
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.q_file = "q_table.npy"

    def choose_action(self, state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.actions))
        if np.random.uniform(0, 1) < self.epsilon:
            return random.randint(0, len(self.actions) - 1)
        return int(np.argmax(self.q_table[state]))

    def update_q_value(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.actions))
        if next_state not in self.q_table:
            self.q_table[next_state] = np.zeros(len(self.actions))
        current_q = self.q_table[state][action]
        max_future_q = np.max(self.q_table[next_state])
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_future_q - current_q)
        self.q_table[state][action] = new_q

    def save_q_table(self):
        np.save(self.q_file, self.q_table)

    def load_q_table(self):
        if os.path.exists(self.q_file):
            self.q_table = np.load(self.q_file, allow_pickle=True).item()
        else:
            self.q_table = {}
