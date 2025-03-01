from flask import Flask, request, jsonify, render_template
import joblib  # Import joblib instead of pickle
import numpy as np

# Load trained model using joblib
model = joblib.load("loan_approval_prediction.pkl")  # No need to use open()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Serves the form

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Get data from JSON request
    
    # Extract features
    features = np.array([
        data["no_of_dependents"], 
        0 if data["education"] == "Graduate" else 1,  
        1 if data["self_employed"] == "Yes" else 0,   
        data["income_annum"],
        data["loan_amount"],
        data["loan_term"],
        data["cibil_score"],
        data["residential_assets_value"],
        data["commercial_assets_value"],
        data["luxury_assets_value"],
        data["bank_asset_value"]
    ]).reshape(1, -1)

    # Make prediction
    prediction = model.predict(features)
    result = "Approved" if prediction[0] == 0 else "Rejected"

    return jsonify({"loan_status": result})

if __name__ == '__main__':
    app.run(port=5000)
