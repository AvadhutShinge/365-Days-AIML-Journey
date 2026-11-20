import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Features: study hours and attendance percentage
X = np.array([
    [1, 40], [2, 45], [3, 50], [3, 60],
    [4, 55], [5, 60], [5, 70], [6, 65],
    [7, 75], [8, 80], [9, 85], [10, 95]
])

# 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Student Performance Prediction")
print("--------------------------------")
print(f"Model Accuracy: {accuracy * 100:.2f}%")

study_hours = float(input("\nEnter study hours: "))
attendance = float(input("Enter attendance percentage: "))

if study_hours < 0 or not 0 <= attendance <= 100:
    raise ValueError("Study hours must be non-negative and attendance must be between 0 and 100.")

student = np.array([[study_hours, attendance]])
result = model.predict(student)[0]

print("Student Result:", "PASS" if result == 1 else "FAIL")
