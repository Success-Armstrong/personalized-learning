# app.py

import streamlit as st
from rl_agent import QLearningAgent
from student_simulator import train_agent
import os
import numpy as np

# Define actions
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

# Theory content mapping
def get_theory_text(topic):
    return {
        "Algebra": "Algebra involves symbols and rules for manipulating those symbols...",
        "Biology": "Biology is the study of living organisms...",
        "History": "History is the study of past events, especially in human affairs..."
    }.get(topic, "No theory content available.")

st.title("🎓 AI-Powered Personalized Learning")
st.subheader("Using Q-Learning to Recommend Study Actions")

student_level = st.selectbox("Select Student Level", ["Beginner", "Intermediate", "Advanced"])
topic = st.selectbox("Select Topic", ["Algebra", "Biology", "History"])

if st.button("Get Recommendation"):
    state = (student_level, topic)

    if state not in agent.q_table:
        agent.q_table[state] = np.zeros(len(actions))

    ai_action_index = agent.choose_action(state)
    ai_action = actions[ai_action_index]

    # Rule-based fallback for display
    expected_actions = {
        "Beginner": "Watch Video",
        "Intermediate": "Practice Quiz",
        "Advanced": "Read Theory"
    }
    expected_action = expected_actions.get(student_level)

    st.success(f"📌 AI Suggested: {ai_action}")
    st.info(f"🧠 Showing learning content based on expected action for {student_level}: **{expected_action}**")

    # Display appropriate learning content
    if expected_action == "Watch Video":
        st.subheader("📺 Recommended Video")
        st.video(get_video_url(topic))

    elif expected_action == "Practice Quiz":
        st.subheader("✅ Practice Quiz")
        st.info("Sample Question: What is the main concept behind this topic?")

    elif expected_action == "Read Theory":
        st.subheader("📄 Reading Material")
        st.write(get_theory_text(topic))

# Optional retraining
if st.button("Retrain Agent"):
    agent = train_agent()
    agent.save_q_table()
    st.success("✅ Agent retrained and Q-table saved.")
