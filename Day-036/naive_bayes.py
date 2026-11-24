# Day 36: Student Performance Prediction using Naive Bayes
# Install dependency: pip install scikit-learn

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# Features: study hours per day and attendance percentage
X = [
    [1, 45], [2, 50], [1.5, 55], [2.5, 60],
    [3, 65], [3.5, 70], [4, 75], [5, 80],
    [5.5, 85], [6, 90], [7, 92], [8, 95],
    [2, 40], [3, 50], [4, 60], [6, 75],
    [7, 80], [1, 35], [5, 70], [8, 88],
]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Student Performance Prediction - Naive Bayes")
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print(classification_report(y_test, y_pred, target_names=["Fail", "Pass"]))

# Predict a new student's result
new_student = [[5, 82]]
prediction = model.predict(new_student)[0]
pass_probability = model.predict_proba(new_student)[0][1]

print("New student prediction:", "PASS" if prediction == 1 else "FAIL")
print(f"Pass probability: {pass_probability * 100:.2f}%")
