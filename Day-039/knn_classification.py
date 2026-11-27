# Day 39 - K-Nearest Neighbors (KNN) Classification

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features using only the training data to avoid data leakage
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train and compare KNN models with different K values
for k in [3, 5, 7]:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"\nK = {k}")
    print(f"Accuracy: {accuracy:.2f}")
    print(classification_report(
        y_test, y_pred, target_names=iris.target_names, zero_division=0
    ))

# Train final model using K = 5
final_model = KNeighborsClassifier(n_neighbors=5)
final_model.fit(X_train_scaled, y_train)

# Predict the species for a new flower sample
sample = [[5.1, 3.5, 1.4, 0.2]]
sample_scaled = scaler.transform(sample)
prediction = final_model.predict(sample_scaled)[0]

print("Predicted flower species:", iris.target_names[prediction])
