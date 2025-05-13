# Save this as train_model.py and run it once
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Sample dummy dataset (replace with your actual dataset)
data = {
    'Age': [25, 40, 35],
    'Diabetes': [0, 1, 0],
    'BloodPressureProblems': [0, 1, 0],
    'AnyTransplants': [0, 0, 1],
    'AnyChronicDiseases': [1, 1, 0],
    'Height': [170, 165, 180],
    'Weight': [70, 80, 75],
    'KnownAllergies': [0, 1, 0],
    'HistoryOfCancerInFamily': [1, 0, 1],
    'NumberOfMajorSurgeries': [1, 2, 0],
    'PremiumPrice': [20000, 32000, 18000]
}
df = pd.DataFrame(data)

X = df.drop('PremiumPrice', axis=1)
y = df['PremiumPrice']

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, 'model.pkl')
