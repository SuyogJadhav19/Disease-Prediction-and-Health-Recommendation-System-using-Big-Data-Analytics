# Disease-Prediction-and-Health-Recommendation-System-using-Big-Data-Analyticsfrom flask import Flask, render_template, request
from pymongo import MongoClient
from model import predict_disease

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["disease_prediction"]
collection = db["predictions"]

symptoms_list = [
    "Fever", "Cough", "Headache", "Fatigue",
    "Nausea", "Vomiting", "Body Pain",
    "Sore Throat", "Breathlessness", "Chills"
]

@app.route('/')
def home():
    return render_template('index.html', symptoms=symptoms_list)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = []

    for symptom in symptoms_list:
        value = request.form.get(symptom)
        input_data.append(1 if value == "on" else 0)

    predictions = predict_disease(input_data)

    # Save to MongoDB
    collection.insert_one({
        "symptoms": input_data,
        "predictions": predictions
    })

    return render_template(
        'result.html',
        predictions=predictions
    )

if __name__ == '__main__':
    app.run(debug=True)
