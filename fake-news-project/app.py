import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📰 Fake News Detector")

input_text = st.text_area("Enter News Text")

if st.button("Check"):
    data = vectorizer.transform([input_text])
    prediction = model.predict(data)

    if prediction[0] == 0:
        st.error("🚨 This is FAKE news")
    else:
        st.success("✅ This is REAL news")