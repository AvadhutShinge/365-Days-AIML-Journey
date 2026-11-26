# Day 38 - Classification Model Evaluation

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train a classification model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate evaluation metrics
print("Classification Model Evaluation")
print("--------------------------------")
print(f"Accuracy:  {accuracy_score(y_test, y_pred):.2f}")
print(
    f"Precision: {precision_score(y_test, y_pred, average='macro'):.2f}"
)
print(f"Recall:    {recall_score(y_test, y_pred, average='macro'):.2f}")
print(f"F1-score:  {f1_score(y_test, y_pred, average='macro'):.2f}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Predict the class of one sample
sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(sample)[0]
print("Sample flower prediction:", iris.target_names[prediction])
