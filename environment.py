# environment.py

# import random

# # Define available actions
# ACTIONS = ["Watch Video", "Practice Quiz", "Read Theory"]

# # Define state space: (topic, student_level)
# TOPICS = ["Algebra", "Photosynthesis", "World War II"]
# LEVELS = ["Beginner", "Intermediate", "Advanced"]

# def get_all_states():
#     """Returns list of all possible (topic, level) state combinations"""
#     return [(topic, level) for topic in TOPICS for level in LEVELS]

# def get_possible_actions():
#     """Returns the list of possible actions"""
#     return ACTIONS

# def simulate_student_response(state, action):
#     """
#     Simulates student response to an action based on state.
#     Returns reward: +1 if good response, -1 if bad response.
#     """
#     topic, level = state
#     base_success = {
#         "Beginner": 0.4,
#         "Intermediate": 0.6,
#         "Advanced": 0.8
#     }
#     # Adjust based on action type
#     action_boost = {
#         "Watch Video": 0.1,
#         "Practice Quiz": 0.2,
#         "Read Theory": 0.05
#     }

#     chance_of_success = base_success[level] + action_boost[action]
#     success = random.random() < chance_of_success
#     return 1 if success else -1


# environment.py

# Define all possible states
def get_all_states():
    levels = ["Beginner", "Intermediate", "Advanced"]
    topics = ["Algebra", "Biology", "History"]
    return [(level, topic) for level in levels for topic in topics]

# Reward system: give +10 for expected action, -5 otherwise
def simulate_student_response(state, action_index):
    student_type, _ = state
    correct_actions = {
        "Beginner": 0,       # Watch Video
        "Intermediate": 1,   # Practice Quiz
        "Advanced": 2        # Read Theory
    }
    correct_action = correct_actions[student_type]
    return 10 if action_index == correct_action else -5
