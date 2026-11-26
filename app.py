import os
import joblib
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Performance Prediction System")
st.write(
    "Predict an estimated exam score using student academic details. "
    "This is an educational demonstration built with Machine Learning."
)

MODEL_PATH = "model/student_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("Trained model not found. Please run: python train_model.py")
    st.stop()

model = joblib.load(MODEL_PATH)

st.divider()
st.subheader("Enter Student Details")

left, right = st.columns(2)

with left:
    study_hours = st.slider("Study Hours Per Day", 0.0, 10.0, 5.0, 0.5)
    attendance = st.slider("Attendance (%)", 40, 100, 75)
    previous_score = st.slider("Previous Exam Score", 0, 100, 70)

with right:
    assignment_score = st.slider("Assignment Score", 0, 100, 75)
    sleep_hours = st.slider("Sleep Hours Per Day", 4.0, 10.0, 7.0, 0.5)

if st.button("Predict Student Performance", type="primary"):
    input_data = pd.DataFrame([{
        "study_hours": study_hours,
        "attendance": attendance,
        "previous_score": previous_score,
        "assignment_score": assignment_score,
        "sleep_hours": sleep_hours
    }])

    prediction = float(model.predict(input_data)[0])
    prediction = max(0.0, min(100.0, prediction))

    st.divider()
    st.subheader("Prediction Result")
    st.metric("Estimated Final Exam Score", f"{prediction:.1f} / 100")

    if prediction >= 75:
        category = "Excellent"
        st.success(f"Performance Category: {category}")
    elif prediction >= 60:
        category = "Good"
        st.info(f"Performance Category: {category}")
    elif prediction >= 40:
        category = "Average"
        st.warning(f"Performance Category: {category}")
    else:
        category = "Needs Improvement"
        st.error(f"Performance Category: {category}")

    fig, ax = plt.subplots()
    ax.bar(["Estimated score"], [prediction])
    ax.set_ylim(0, 100)
    ax.set_ylabel("Marks")
    ax.set_title("Student Performance Prediction")
    st.pyplot(fig)
    plt.close(fig)

    st.caption(
        "Note: This estimate comes from a model trained on synthetic sample data. "
        "It is for educational demonstration only and is not a validated prediction "
        "of a real student's exam result."
    )

with st.expander("About this project"):
    st.write(
        "Algorithm: Random Forest Regression. "
        "Inputs: study hours, attendance, previous score, assignment score, and sleep hours. "
        "Libraries: Pandas, NumPy, Scikit-learn, Joblib, Matplotlib, and Streamlit."
    )
