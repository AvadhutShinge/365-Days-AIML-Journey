import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Input features: study hours and attendance percentage
X = np.array([
    [1, 40], [2, 45], [2, 55], [3, 50], [3, 60],
    [4, 45], [4, 55], [4, 60], [5, 50], [5, 60],
    [5, 70], [6, 65], [6, 75], [7, 70], [7, 80],
    [8, 75], [8, 85], [9, 80], [9, 90], [10, 95]
])

# Target: 0 = Fail, 1 = Pass
y = np.array([
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1
])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Create and train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Student Performance Prediction")
print("--------------------------------")
print(f"Model accuracy: {accuracy * 100:.2f}%")
print("\nClassification report:")
print(classification_report(
    y_test, y_pred, target_names=["Fail", "Pass"], zero_division=0
))

# Predict for a new student
study_hours = float(input("\nEnter study hours: "))
attendance = float(input("Enter attendance percentage: "))

if study_hours < 0 or not 0 <= attendance <= 100:
    raise ValueError("Study hours must be non-negative and attendance must be 0 to 100.")

student = np.array([[study_hours, attendance]])
prediction = model.predict(student)[0]
probability = model.predict_proba(student)[0]

print("\nPrediction:", "PASS" if prediction == 1 else "FAIL")
print(f"Pass probability: {probability[1] * 100:.2f}%")
