import streamlit as st

# Function to calculate the score
def calculate_score(glucose_level, blood_pressure, weight, symptoms, diet, exercise):
    score = 0
    
    # Evaluate glucose level
    if glucose_level > 180:
        score += 2
    elif glucose_level > 140:
        score += 1
    
    # Evaluate blood pressure
    if blood_pressure > 140:
        score += 2
    elif blood_pressure > 120:
        score += 1
    
    # Evaluate weight
    if weight > 200:  # Example threshold
        score += 2
    elif weight > 180:
        score += 1
    
    # Evaluate symptoms
    if symptoms:
        score += len(symptoms)
    
    # Evaluate diet
    if diet == "Poor":
        score += 2
    elif diet == "Average":
        score += 1
    
    # Evaluate exercise
    if exercise == "None":
        score += 2
    elif exercise == "Occasional":
        score += 1
    
    return score

# Streamlit app
st.title("Chronic Care Management for Type 2 Diabetes")
st.write("""
This application helps individuals with Type 2 diabetes manage their chronic condition by evaluating various ongoing health concerns and producing a score. The score provides guidance on whether to seek medical advice.
""")

# User inputs
st.header("Enter Your Health Data")

glucose_level = st.number_input("Fasting Blood Glucose Level (mg/dL)", min_value=0, max_value=500, step=1)
blood_pressure = st.number_input("Blood Pressure (Systolic mmHg)", min_value=0, max_value=300, step=1)
weight = st.number_input("Weight (lbs)", min_value=0, max_value=500, step=1)

st.subheader("Check any of the following symptoms:")
symptoms = st.multiselect("Symptoms", ["Fatigue", "Increased Thirst", "Frequent Urination", "Blurred Vision", "Slow Healing Wounds"])

diet = st.radio("How would you rate your diet?", ["Good", "Average", "Poor"])
exercise = st.radio("How often do you exercise?", ["Regular", "Occasional", "None"])

# Calculate score
score = calculate_score(glucose_level, blood_pressure, weight, symptoms, diet, exercise)

# Display result
st.header("Your Health Score")
st.write(f"Your score is: {score}")

if score >= 5:
    st.error("Your score indicates that you should contact your doctor.")
else:
    st.success("Your score indicates that you do not need to contact your doctor at this time.")
