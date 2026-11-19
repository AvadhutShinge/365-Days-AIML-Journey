import numpy as np
from sklearn.linear_model import LogisticRegression

# Input: study hours
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)

# Output: 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Create and train the Logistic Regression model
model = LogisticRegression()
model.fit(X, y)

# Get study hours from the user
hours = float(input("Enter study hours: "))

if hours < 0:
    raise ValueError("Study hours cannot be negative.")

student = np.array([[hours]])

# Predict pass or fail
prediction = model.predict(student)[0]
pass_probability = model.predict_proba(student)[0][1]

print("\nStudent Pass/Fail Prediction")
print("----------------------------")
print("Study Hours:", hours)
print("Prediction:", "PASS" if prediction == 1 else "FAIL")
print(f"Pass Probability: {pass_probability * 100:.2f}%")
