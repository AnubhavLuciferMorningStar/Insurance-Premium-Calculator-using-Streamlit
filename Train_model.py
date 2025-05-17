import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Define file path
file_path = 'C:/Users/dell/OneDrive/Desktop/Scaler Certificates/Project Portfolio/Insurance Cost Prediction/insurance.csv'

# Load dataset
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
    exit(1)
except Exception as e:
    print(f"Error reading CSV: {e}")
    exit(1)

# Define required columns
required_columns = [
    'Age', 'Diabetes', 'BloodPressureProblems', 'AnyTransplants', 'AnyChronicDiseases',
    'Height', 'Weight', 'KnownAllergies', 'HistoryOfCancerInFamily', 'NumberOfMajorSurgeries', 'PremiumPrice'
]

# Verify columns
if not all(col in data.columns for col in required_columns):
    print(f"Error: CSV must contain these columns: {required_columns}")
    print(f"Found columns: {list(data.columns)}")
    exit(1)

# Prepare features and target
X = data.drop('PremiumPrice', axis=1)
y = data['PremiumPrice']

# Train model
try:
    model = RandomForestRegressor()
    model.fit(X, y)
except Exception as e:
    print(f"Error training model: {e}")
    exit(1)

# Save model
try:
    joblib.dump(model, 'model.pkl')
    print("Model trained and saved as model.pkl")
except Exception as e:
    print(f"Error saving model: {e}")
    exit(1)