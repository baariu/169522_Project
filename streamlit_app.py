import streamlit as st
import requests

# Replace with your actual Render FastAPI URL
API_URL = "https://one69522-project-912g.onrender.com/predict"

# Streamlit UI
st.title("🚀 FastAPI ML Model - Streamlit Frontend")
st.write("Enter feature values and get a prediction.")

# Input fields
feature1 = st.number_input("Feature 1", value=0.0)
feature2 = st.number_input("Feature 2", value=0.0)
feature3 = st.number_input("Feature 3", value=0.0)
feature4 = st.number_input("Feature 4", value=0.0)

# Button to make API request
if st.button("Predict"):
    data = {"features": [feature1, feature2, feature3, feature4]}
    
    # Send request to FastAPI backend
    response = requests.post(API_URL, json=data)
    
    if response.status_code == 200:
        prediction = response.json().get("prediction", "No prediction returned")
        st.success(f"Prediction: {prediction}")
    else:
        st.error("Error making request. Check the API.")

