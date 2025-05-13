import streamlit as st
import requests

st.title("💡 Insurance Premium Calculator")

age = st.slider("Age", 18, 100, 30)
diabetes = st.selectbox("Diabetes", ['No', 'Yes'])
bp = st.selectbox("Blood Pressure Problems", ['No', 'Yes'])
transplant = st.selectbox("Any Transplants", ['No', 'Yes'])
chronic = st.selectbox("Any Chronic Diseases", ['No', 'Yes'])
height = st.slider("Height (cm)", 145, 188, 170)
weight = st.slider("Weight (kg)", 51, 132, 70)
allergy = st.selectbox("Known Allergies", ['No', 'Yes'])
cancer = st.selectbox("Family Cancer History", ['No', 'Yes'])
surgeries = st.slider("Number of Major Surgeries", 0, 3, 1)

# Convert string options to binary
def to_binary(option):
    return 1 if option == 'Yes' else 0

if st.button("Estimate Premium"):
    payload = {
        "Age": age,
        "Diabetes": to_binary(diabetes),
        "BloodPressureProblems": to_binary(bp),
        "AnyTransplants": to_binary(transplant),
        "AnyChronicDiseases": to_binary(chronic),
        "Height": height,
        "Weight": weight,
        "KnownAllergies": to_binary(allergy),
        "HistoryOfCancerInFamily": to_binary(cancer),
        "NumberOfMajorSurgeries": surgeries
    }

    try:
        response = requests.post("http://localhost:5000/predict", json=payload)
        response.raise_for_status()  # Catch HTTP errors
        result = response.json()
        st.success(f"Estimated Premium: ₹ {result['EstimatedPremium']}")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Failed to get prediction from API.\n\n**Details:** {e}")
