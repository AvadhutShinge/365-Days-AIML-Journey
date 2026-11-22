import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Features: study hours and attendance percentage
X = np.array([
    [1, 35], [2, 40], [2, 50], [3, 45],
    [3, 55], [4, 50], [4, 60], [5, 55],
    [5, 65], [6, 70], [6, 75], [7, 70],
    [7, 80], [8, 85], [9, 90], [10, 95]
])

# Target: 0 = Fail, 1 = Pass
y = np.array([
    0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1, 1, 1
])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Scale features and train a KNN classifier
model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=3)
)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Student Performance Prediction using KNN")
print("-----------------------------------------")
print(f"Model accuracy: {accuracy * 100:.2f}%")

# Get details for a new student
study_hours = float(input("\nEnter study hours: "))
attendance = float(input("Enter attendance percentage: "))

if study_hours < 0 or not 0 <= attendance <= 100:
    raise ValueError("Study hours must be non-negative and attendance must be 0 to 100.")

student = np.array([[study_hours, attendance]])
prediction = model.predict(student)[0]
probability = model.predict_proba(student)[0]

print("\nPrediction:", "PASS" if prediction == 1 else "FAIL")
print(f"Pass probability: {probability[1] * 100:.2f}%")
