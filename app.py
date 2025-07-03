# app.py

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


import streamlit as st
from student_simulator import train_agent
from rl_agent import QLearningAgent
import os

st.set_page_config(page_title="AI Personalized Learning", layout="centered")
st.title("🎓 AI-Powered Personalized Learning")
st.subheader("Using Q-Learning to Recommend Study Actions")

student_level = st.selectbox("Select Student Level", ["Beginner", "Intermediate", "Advanced"])
topic = st.selectbox("Select Topic", ["Algebra", "Photosynthesis", "World War II"])
state = (topic, student_level)

# Load or train the agent
if os.path.exists("q_table.npy"):
    agent = QLearningAgent()
    agent.load_q_table()
else:
    with st.spinner("Training RL Agent..."):
        agent = train_agent()
        agent.save_q_table()

if st.button("Get Recommendation"):
    action = agent.choose_action(state)
    st.success(f"Recommended next activity: **{action}** for a {student_level} student learning **{topic}**")
