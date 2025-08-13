import streamlit as st
import pandas as pd
import joblib
import numpy as np

b0 = 55.22479999999996  # Intercept
b1 = 1.11405182    # Hours Studied
b2 = 4.26701452   # Previous Scores
b3 = 18.97811168  # Extracurricular Activities (0 or 1)
b4 = -2.7198889    # Sleep Hours
b5 = 61.26684686  # Sample Question Papers Practiced

min_values = joblib.load("min_value.pkl")
max_values = joblib.load("max_value.pkl")
pca = joblib.load("student_perf_pipeline.pkl")

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

user_input = {
    "hours_studied" : hours_studied,
    "prev_scores" : prev_scores,
    "extra_activities" : extra_activities_num,
    "sleep_hours" : sleep_hours,
    "sample_questions" : sample_questions
}

normalized_data = pd.DataFrame([{
    "Hours Studied" : (user_input["hours_studied"] - min_values["Hours Studied"])/(max_values["Hours Studied"] - min_values["Hours Studied"]),
    "Previous Scores" : (user_input["prev_scores"] - min_values["Previous Scores"])/(max_values["Previous Scores"] - min_values["Previous Scores"]),
    "Extracurricular Activities" : (user_input["extra_activities"] - min_values["Extracurricular Activities"])/(max_values["Extracurricular Activities"] - min_values["Extracurricular Activities"]),
    "Sleep Hours" : (user_input["sleep_hours"] - min_values["Sleep Hours"])/(max_values["Sleep Hours"] - min_values["Sleep Hours"]),
    "Sample Question Papers Practiced" : (user_input["sample_questions"] - min_values["Sample Question Papers Practiced"])/(max_values["Sample Question Papers Practiced"] - min_values["Sample Question Papers Practiced"])

}])

normalized_data = pca.transform(normalized_data)

# Predict
if st.button("Predict Performance Index"):
    performance_index = b0 + np.dot(normalized_data, np.array([b1,b2,b3,b4,b5]))
    
    st.success(f"📈 Predicted Performance Index: {performance_index}")
