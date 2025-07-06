# app.py

import streamlit as st
from rl_agent import QLearningAgent
from student_simulator import train_agent
import os
import numpy as np

# Define possible actions
actions = ["Watch Video", "Practice Quiz", "Read Theory"]

# Initialize agent
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

# Reading material mapping
def get_theory_text(topic):
    return {
        "Algebra": "Algebra involves symbols and rules for manipulating those symbols...",
        "Biology": "Biology is the study of living organisms...",
        "History": "History is the study of past events, especially in human affairs..."
    }.get(topic, "No theory content available.")

# Streamlit UI
st.title("🎓 AI-Powered Personalized Learning")
st.subheader("Using Q-Learning to Recommend Study Actions")

# User selects level and topic
student_level = st.selectbox("Select Student Level", ["Beginner", "Intermediate", "Advanced"])
topic = st.selectbox("Select Topic", ["Algebra", "Biology", "History"])

if st.button("Get Recommendation"):
    state = (student_level, topic)

    # Ensure state exists in Q-table
    if state not in agent.q_table:
        agent.q_table[state] = np.zeros(len(actions))

    action_index = agent.choose_action(state)
    action = actions[action_index]

    st.success(f"📌 Recommended Action: {action}")

    # Display based on student level
    if student_level == "Beginner" and action == "Watch Video":
        st.subheader("📺 Recommended Video")
        video_url = get_video_url(topic)
        st.video(video_url)

    elif student_level == "Intermediate" and action == "Practice Quiz":
        st.subheader("✅ Practice Quiz")
        st.info("Quiz coming soon! For now, try answering: What is the core concept of this topic?")

    elif student_level == "Advanced" and action == "Read Theory":
        st.subheader("📄 Reading Material")
        theory_text = get_theory_text(topic)
        st.write(theory_text)

    else:
        st.warning("🤔 The recommendation doesn't match the expected learning path for this level.")

# Optional: retrain agent
if st.button("Retrain Agent"):
    agent = train_agent()
    agent.save_q_table()
    st.success("✅ Agent retrained and Q-table saved.")
