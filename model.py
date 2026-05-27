import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("dataset.csv")

X = df.drop("Disease", axis=1)
y = df["Disease"]

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

def predict_disease(data):
    probabilities = model.predict_proba([data])[0]
    classes = model.classes_

    results = []

    for disease, prob in zip(classes, probabilities):
        results.append((disease, round(prob * 100, 2)))

    results.sort(key=lambda x: x[1], reverse=True)

    return results[:3]
