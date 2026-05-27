# Disease Prediction and Health Recommendation System using Big Data Analytics

## 📌 Project Overview
This project is a Disease Prediction and Health Recommendation System developed using Big Data Analytics and Machine Learning techniques.

The system predicts possible diseases based on user-selected symptoms and provides health recommendations in real time through a web interface.

The project integrates:
- Flask for web development
- PySpark for big data processing
- Scikit-learn for machine learning
- MongoDB for database storage

---

# 🚀 Features
- Predict diseases based on symptoms
- Real-time prediction using Machine Learning
- Big Data processing with PySpark
- Stores prediction history in MongoDB
- User-friendly Bootstrap interface
- Displays Top-3 disease predictions with confidence scores

---

# 🛠 Technologies Used

## Backend
- Python 3.x
- Flask

## Machine Learning
- Scikit-learn
- Random Forest Classifier

## Big Data
- PySpark

## Database
- MongoDB

## Frontend
- HTML
- Bootstrap

---

# 📂 Project Structure

```txt
DiseasePredictionProject/
│
├── app.py
├── model.py
├── spark_processing.py
├── generate_dataset.py
├── dataset.csv
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── result.html
```

---

# 📊 Dataset Information

The dataset contains:
- 10 symptom features
- 8 disease classes
- Binary values (0 or 1)

## Symptoms Used
- Fever
- Cough
- Headache
- Fatigue
- Nausea
- Vomiting
- Body Pain
- Sore Throat
- Breathlessness
- Chills

## Diseases Predicted
- Flu
- COVID-19
- Migraine
- Food Poisoning
- Pneumonia
- Cold
- Asthma
- Malaria

---

# ⚙ Installation and Setup

## Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/disease-prediction-system.git
```

---

## Step 2: Navigate to Project Folder

```bash
cd disease-prediction-system
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄 MongoDB Setup

1. Install MongoDB Community Server
2. Start MongoDB service

Default MongoDB URL:

```txt
mongodb://localhost:27017/
```

---

# ▶ Running the Project

## Step 1: Generate Dataset

```bash
python generate_dataset.py
```

---

## Step 2: Run PySpark Processing (Optional)

```bash
python spark_processing.py
```

---

## Step 3: Start Flask Application

```bash
python app.py
```

---

## Step 4: Open Browser

```txt
http://127.0.0.1:5000
```

---

# 🧠 Machine Learning Model

The system uses:
- Random Forest Classifier

### Why Random Forest?
- High accuracy
- Handles multiple classes effectively
- Reduces overfitting
- Works well with structured datasets

---

# 📈 Output Example

## Input Symptoms
- Fever
- Cough
- Body Pain

## Predicted Diseases

| Disease | Confidence |
|---|---|
| Flu | 87% |
| COVID-19 | 75% |
| Pneumonia | 60% |

---

# 🧪 Testing Performed

## Unit Testing
- Model prediction testing
- Data preprocessing testing

## Integration Testing
- Frontend → Backend → Model → Database

## System Testing
- Full application workflow tested

---

# 🔮 Future Enhancements
- Integration with real healthcare datasets
- Deep Learning implementation
- Real-time data streaming using Kafka
- Mobile application development
- Cloud deployment using AWS/Azure
- Wearable device integration

---

# 📌 Conclusion

This project demonstrates the successful integration of:
- Big Data Analytics
- Machine Learning
- Web Development
- Database Management

for intelligent healthcare prediction systems.

The project provides scalable and real-time disease prediction capabilities and can be extended for real-world healthcare applications.

---

# 📚 References

- https://scikit-learn.org
- https://spark.apache.org/docs/latest/api/python/
- https://flask.palletsprojects.com
- https://www.mongodb.com/docs/
- https://getbootstrap.com/docs/
