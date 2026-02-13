3.65 kB
import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(page_title="FitPlan AI", layout="centered")

st.title(" FitPlan AI – User Fitness Profile")

# ---------------------------------------------------
# PERSONAL INFORMATION
# ---------------------------------------------------
st.subheader("👤 Personal Information")

name = st.text_input("Enter Your Name")

st.subheader("Gender")

gender = st.radio(
    "",
    ["Male", "Female"],
    horizontal=True,index=0
)


col1, col2 = st.columns(2)

with col1:
    height = st.number_input("Height (in cm)", min_value=100, max_value=250)

with col2:
    weight = st.number_input("Weight (in kg)", min_value=30, max_value=200)

# ---------------------------------------------------
# BMI CALCULATION
# ---------------------------------------------------
bmi = None

if height > 0 and weight > 0:
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    st.write(f"### 📊 Your BMI: {bmi:.2f}")

# ---------------------------------------------------
# FITNESS GOAL
# ---------------------------------------------------
st.subheader("🎯 Fitness Goal")

goal = st.selectbox(
    "",
    [
        "Flexible",
        "Weight Loss",
        "Build Muscle",
        "Strength Gaining",
        "Abs Building"
    ]
)

st.subheader("🏋️ Available Equipment")

equipment_map = {}

col1, col2, col3 = st.columns(3)

with col1:
    equipment_map["No Equipment"] = st.checkbox("No Equipment")
    equipment_map["Pull-up Bar"] = st.checkbox("Pull-up Bar")
    equipment_map["Dip Bars"] = st.checkbox("Dip Bars")
    equipment_map["Push-up Handles"] = st.checkbox("Push-up Handles")
    equipment_map["Dumbbells"] = st.checkbox("Dumbbells")
    equipment_map["Adjustable Dumbbells"] = st.checkbox("Adjustable Dumbbells")

with col2:
    equipment_map["Barbell"] = st.checkbox("Barbell")
    equipment_map["Weight Plates"] = st.checkbox("Weight Plates")
    equipment_map["Kettlebells"] = st.checkbox("Kettlebells")
    equipment_map["Medicine Ball"] = st.checkbox("Medicine Ball")
    equipment_map["Yoga Mat"] = st.checkbox("Yoga Mat")
    equipment_map["Resistance Band"] = st.checkbox("Resistance Band")

with col3:
    equipment_map["Bosu Ball"] = st.checkbox("Bosu Ball")
    equipment_map["Stability Ball"] = st.checkbox("Stability Ball")
    equipment_map["Foam Roller"] = st.checkbox("Foam Roller")
    equipment_map["Treadmill"] = st.checkbox("Treadmill")
    equipment_map["Exercise Bike"] = st.checkbox("Exercise Bike")
    equipment_map["Skipping Rope"] = st.checkbox("Skipping Rope")

# Convert selected to list
equipment = [item for item, selected in equipment_map.items() if selected]


# ---------------------------------------------------
# FITNESS LEVEL
# ---------------------------------------------------
st.subheader("📈 Fitness Level")

fitness_level = st.radio(
    "",
    ["Beginner", "Intermediate", "Advanced"],
    horizontal=True
)

# ---------------------------------------------------
# SUBMIT BUTTON
# ---------------------------------------------------
if st.button("Submit Profile"):

    if not name:
        st.error("Please enter your name.")
    elif not equipment:
        st.error("Please select at least one equipment option.")
    else:
        st.success("✅ Profile Submitted Successfully!")

        st.json({
            "Name": name,
            "Gender": gender,
            "BMI": round(bmi, 2) if bmi else None,
            "Goal": goal,
            "Fitness Level": fitness_level,
            "Equipment": equipment
        })
