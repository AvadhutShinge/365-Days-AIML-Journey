import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Student study hours
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)

# Student marks
marks = np.array([20, 25, 35, 40, 50, 55, 65, 70, 80, 90])

# Create model
model = LinearRegression()

# Train model
model.fit(hours, marks)

# Predict marks
study_hours = np.array([[6.5]])
prediction = model.predict(study_hours)

print("Student Marks Prediction System")
print("--------------------------------")
print("Study Hours:", study_hours[0][0])
print("Predicted Marks:", round(prediction[0], 2))

# Display graph
plt.scatter(hours, marks, color="blue", label="Actual Marks")
plt.plot(hours, model.predict(hours), color="red", label="Prediction Line")

plt.xlabel("Study Hours")
plt.ylabel("Student Marks")
plt.title("Student Marks Prediction using Linear Regression")
plt.legend()
plt.show()