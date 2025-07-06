# app.py

import streamlit as st
from rl_agent import QLearningAgent
from student_simulator import train_agent
import os
import numpy as np

# Define actions
actions = ["Watch Video", "Practice Quiz", "Read Theory"]

# Initialize the agent and load Q-table
agent = QLearningAgent(actions)
agent.load_q_table()

# Video content mapping
def get_video_url(topic):
    video_library = {
        "Algebra": "https://www.youtube.com/embed/HEfHFsfGXjs",
        "Biology": "https://www.youtube.com/embed/Uz5cCI5bznk",
        "History": "https://www.youtube.com/embed/dlB4T9RJSSo"
    }
    return video_library.get(topic, "")

# Streamlit app interface
st.title("🎓 AI-Powered Personalized Learning")
st.subheader("Using Q-Learning to Recommend Study Actions")

# User inputs
student_level = st.selectbox("Select Student Level", ["Beginner", "Intermediate", "Advanced"])
topic = st.selectbox("Select Topic", ["Algebra", "Biology", "History"])

if st.button("Get Recommendation"):
    state = (student_level, topic)

    # Ensure Q-table has entry for this state
    if state not in agent.q_table:
        agent.q_table[state] = np.zeros(len(actions))

    action_index = agent.choose_action(state)
    action = actions[action_index]

    st.success(f"📌 Recommended Action: {action}")

    # Show embedded video if action is "Watch Video"
    if action == "Watch Video":
        st.subheader("📺 Recommended Video")
        video_url = get_video_url(topic)
        if video_url:
            st.video(video_url)
        else:
            st.info("No video available for this topic.")

# Optional: train the agent from UI
if st.button("Retrain Agent"):
    agent = train_agent()
    agent.save_q_table()
    st.success("✅ Agent retrained and Q-table saved.")
