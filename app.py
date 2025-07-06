import streamlit as st
from rl_agent import QLearningAgent

# Setup
actions = ["Watch Video", "Practice Quiz", "Read Theory"]
agent = QLearningAgent(actions)

# Try loading Q-table
try:
    agent.load_q_table()
except Exception as e:
    st.warning(f"Could not load Q-table: {e}")

# UI
st.title("🎓 AI-Powered Personalized Learning")
st.subheader("Using Q-Learning to Recommend Study Actions")

student_level = st.selectbox("Select Student Level", ["Beginner", "Intermediate", "Advanced"])
subject = st.selectbox("Select Topic", ["Algebra", "Biology", "History"])

if st.button("Recommend Study Action"):
    state = (student_level, subject)
    action_index = agent.choose_action(state)
    recommendation = actions[action_index]
    st.success(f"Recommended Activity: **{recommendation}**")

# Option to save Q-table (can be placed elsewhere)
try:
    agent.save_q_table()
except Exception as e:
    st.warning(f"Could not save Q-table: {e}")
