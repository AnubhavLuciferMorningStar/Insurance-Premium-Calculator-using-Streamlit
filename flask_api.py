from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([[
        data['Age'],
        data['Diabetes'],
        data['BloodPressureProblems'],
        data['AnyTransplants'],
        data['AnyChronicDiseases'],
        data['Height'],
        data['Weight'],
        data['KnownAllergies'],
        data['HistoryOfCancerInFamily'],
        data['NumberOfMajorSurgeries']
    ]])
    prediction = model.predict(features)[0]
    return jsonify({'EstimatedPremium': round(prediction, 2)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
