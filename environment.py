# environment.py

import random

# Define available actions
ACTIONS = ["Watch Video", "Practice Quiz", "Read Theory"]

# Define state space: (topic, student_level)
TOPICS = ["Algebra", "Photosynthesis", "World War II"]
LEVELS = ["Beginner", "Intermediate", "Advanced"]

def get_all_states():
    """Returns list of all possible (topic, level) state combinations"""
    return [(topic, level) for topic in TOPICS for level in LEVELS]

def get_possible_actions():
    """Returns the list of possible actions"""
    return ACTIONS

def simulate_student_response(state, action):
    """
    Simulates student response to an action based on state.
    Returns reward: +1 if good response, -1 if bad response.
    """
    topic, level = state
    base_success = {
        "Beginner": 0.4,
        "Intermediate": 0.6,
        "Advanced": 0.8
    }
    # Adjust based on action type
    action_boost = {
        "Watch Video": 0.1,
        "Practice Quiz": 0.2,
        "Read Theory": 0.05
    }

    chance_of_success = base_success[level] + action_boost[action]
    success = random.random() < chance_of_success
    return 1 if success else -1
