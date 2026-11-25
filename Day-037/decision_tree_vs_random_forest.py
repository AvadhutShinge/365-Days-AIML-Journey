# Day 37: Decision Tree vs Random Forest
# Compare two machine learning classification algorithms.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the Iris flower dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create and train a Decision Tree model
decision_tree = DecisionTreeClassifier(random_state=42)
decision_tree.fit(X_train, y_train)

# Create and train a Random Forest model
random_forest = RandomForestClassifier(
    n_estimators=100, random_state=42
)
random_forest.fit(X_train, y_train)

# Make predictions
dt_predictions = decision_tree.predict(X_test)
rf_predictions = random_forest.predict(X_test)

# Compare model accuracy
dt_accuracy = accuracy_score(y_test, dt_predictions)
rf_accuracy = accuracy_score(y_test, rf_predictions)

print("Decision Tree Accuracy:", round(dt_accuracy * 100, 2), "%")
print("Random Forest Accuracy:", round(rf_accuracy * 100, 2), "%")

print("\nDecision Tree Classification Report:")
print(classification_report(y_test, dt_predictions, target_names=iris.target_names))

print("Random Forest Classification Report:")
print(classification_report(y_test, rf_predictions, target_names=iris.target_names))

# Predict the flower type for one new example
sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = random_forest.predict(sample)[0]
print("Predicted flower using Random Forest:", iris.target_names[prediction])
