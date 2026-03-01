import streamlit as st
from model_api import query_model
from prompt_builder import build_prompt

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="FitPlan AI", layout="centered")

st.title("🏋️ FitPlan AI — Personalized Workout Generator")
st.write("Fill your fitness details to generate a personalized AI workout plan.")

# ---------------- USER INPUT ---------------- #

name = st.text_input("Name *")

age = st.number_input(
    "Age (years) *",
    min_value=10,
    max_value=100,
    step=1
)

gender = st.radio("Gender *", ["Male", "Female"])

height = st.number_input(
    "Height (cm) *",
    min_value=100.0,
    max_value=250.0
)

weight = st.number_input(
    "Weight (kg) *",
    min_value=30.0,
    max_value=200.0
)

goal = st.selectbox(
    "Fitness Goal",
    ["Build Muscle", "Lose Weight", "Improve Endurance", "General Fitness"]
)

fitness_level = st.radio(
    "Fitness Level",
    ["Beginner", "Intermediate", "Advanced"]
)

equipment = st.multiselect(
    "Available Equipment",
    [
        "No Equipment", "Dumbbells", "Barbell",
        "Pull-up Bar", "Resistance Bands",
        "Treadmill", "Kettlebells", "Full Gym"
    ]
)

# ---------------- GENERATE PLAN ---------------- #

if st.button("Generate Workout Plan"):

    # -------- VALIDATION --------
    if not name.strip():
        st.warning("Please enter your name.")

    elif height <= 0 or weight <= 0:
        st.warning("Please enter valid height and weight.")

    elif not equipment:
        st.warning("Please select at least one equipment option.")

    else:
        # Build prompt + BMI calculation
        prompt, bmi, bmi_status = build_prompt(
            name,
            age,
            gender,
            height,
            weight,
            goal,
            fitness_level,
            equipment
        )

        # AI call
        with st.spinner("Generating your personalized plan..."):
            response = query_model(prompt)

        # -------- OUTPUT --------
        st.subheader("📋 Your Personalized Workout Plan")
        st.write(response)

        st.info(
            f"""
            **Profile Summary**
            - Name: {name}
            - Age: {age}
            - Gender: {gender}
            - BMI: {bmi:.2f} ({bmi_status})
            - Goal: {goal}
            - Level: {fitness_level}
            - Equipment: {', '.join(equipment)}
            """
        )
