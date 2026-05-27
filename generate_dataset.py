import pandas as pd
import random

diseases = {
    "Flu": [1,1,1,1,0,0,1,1,0,1],
    "COVID-19": [1,1,1,1,0,0,1,1,1,1],
    "Migraine": [0,0,1,1,1,0,0,0,0,0],
    "Food Poisoning": [0,0,0,1,1,1,1,0,0,0],
    "Pneumonia": [1,1,0,1,0,0,1,0,1,1],
    "Cold": [0,1,0,0,0,0,0,1,0,1],
    "Asthma": [0,0,0,1,0,0,0,0,1,0],
    "Malaria": [1,0,1,1,1,0,1,0,0,1]
}

columns = [
    "Fever", "Cough", "Headache", "Fatigue",
    "Nausea", "Vomiting", "Body Pain",
    "Sore Throat", "Breathlessness", "Chills"
]

data = []

for disease, symptoms in diseases.items():
    for _ in range(50):
        noisy = [
            min(1, max(0, val + random.choice([-1,0,0,0,1])))
            for val in symptoms
        ]

        row = noisy + [disease]
        data.append(row)

df = pd.DataFrame(data, columns=columns + ["Disease"])

df.to_csv("dataset.csv", index=False)

print("Dataset generated successfully!")
