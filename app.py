import streamlit as st
import numpy as np
import pickle

from study_planner import generate_study_plan
from timetable_generator import generate_timetable

# =========================
# Load Model
# =========================
model = pickle.load(open("model.pkl", "rb"))

# =========================
# Page Config
# =========================
st.set_page_config(page_title="Smart Study Planner", layout="wide")

# =========================
# Title
# =========================
st.markdown("<h1 style='text-align:center;'>🎓 Smart Study Planner</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>AI-powered Study Recommendation & Timetable Generator</p>", unsafe_allow_html=True)

# =========================
# Input Section
# =========================
col1, col2 = st.columns(2)

with col1:
    study_hours = st.number_input("📚 Study Hours", 1, 24, 5)
    attendance = st.number_input("📊 Attendance (%)", 0, 100, 75)
    motivation = st.number_input("🔥 Motivation (0 or 1)", 0, 1, 1)

with col2:
    stress = st.number_input("😓 Stress Level (0 or 1)", 0, 1, 0)
    attention = st.number_input("🧠 Attention Span (minutes)", 10, 120, 30)

    time_pref = st.selectbox(
        "⏰ Preferred Study Time",
        ["Morning", "Afternoon", "Evening", "Night"]
    )

# Additional Inputs
learning_style_option = st.selectbox(
    "🧠 Learning Style (Optional)",
    ["Auto Detect (Recommended)", "Video Learner", "Practice Learner", "Text Learner", "Group Learner", "Mixed Learner"]
)

focus_subject = st.text_input("🎯 Subject to Focus", "Math")
subjects = st.text_input("📘 Subjects (comma separated)", "Math, DSA, OS")

wake = st.time_input("🌅 Wake Time")
sleep = st.time_input("🌙 Sleep Time")

# =========================
# Generate Plan
# =========================
if st.button("🚀 Generate Study Plan"):

    # Prepare input
    input_data = np.array([[
        study_hours,
        attendance,
        motivation,
        stress
    ]])

    # =========================
    # Learning Style
    # =========================
    if learning_style_option == "Auto Detect (Recommended)":
        pred = model.predict(input_data)[0]

        style_map = {
            0: "Video Learner",
            1: "Practice Learner",
            2: "Text Learner",
            3: "Group Learner",
            4: "Mixed Learner"
        }

        learning_style = style_map.get(pred, "Mixed Learner")

    else:
        learning_style = learning_style_option

    st.success(f"🧠 Learning Style Used: {learning_style}")

    # =========================
    # Subjects Handling
    # =========================
    subject_list = [s.strip() for s in subjects.split(",")]

    if focus_subject in subject_list:
        subject_list.remove(focus_subject)

    subject_list.insert(0, focus_subject)

    # =========================
    # Study Plan
    # =========================
    plan = generate_study_plan(
        learning_style,
        subject_list,
        attention,
        time_pref,
        focus_subject
    )

    st.subheader("📚 Study Plan")
    for p in plan:
        st.write("•", p)

    # =========================
    # Timetable
    # =========================
    timetable = generate_timetable(
        wake.strftime("%H:%M"),
        sleep.strftime("%H:%M"),
        study_hours,
        subject_list
    )

    st.subheader("⏰ Daily Timetable")
    for t in timetable:
        st.write(f"{t['start']} - {t['end']} → {t['subject']}")

# =========================
# Footer
# =========================
st.markdown("---")
st.markdown("Made with ❤️ by Pragyan | AI Smart Study Planner")