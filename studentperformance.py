import streamlit as st

b0 = 0.16488379059250907  # Intercept
b1 = 0.18454093    # Hours Studied
b2 = 0.41448703   # Previous Scores
b3 = 0.00783829   # Extracurricular Activities (0 or 1)
b4 = 0.04036962   # Sleep Hours
b5 = 0.03932099   # Sample Question Papers Practiced

# Streamlit App
st.set_page_config(page_title="Student Performance Predictor", layout="centered")
st.title("🎓 Student Performance Index Predictor")

st.write("Enter the following inputs to estimate the student's performance index.")

hours_studied = st.number_input("Hours Studied per Day", min_value=0.0, format="%.2f")
prev_scores = st.number_input("Average of Previous Scores", min_value=0.0, format="%.2f")
extra_activities = st.selectbox("Involved in Extracurricular Activities?", ["Yes", "No"])
sleep_hours = st.number_input("Sleep Hours per Day", min_value=0.0, format="%.2f")
sample_questions = st.number_input("Number of Sample Question Papers Practiced", min_value=0, step=1)

# Convert categorical to numerical
extra_activities_num = 1 if extra_activities == "Yes" else 0

# Predict
if st.button("Predict Performance Index"):
    performance_index = (
        b0 +
        b1 * hours_studied +
        b2 * prev_scores +
        b3 * extra_activities_num +
        b4 * sleep_hours +
        b5 * sample_questions
    )
    st.success(f"📈 Predicted Performance Index: {performance_index:.2f}")
