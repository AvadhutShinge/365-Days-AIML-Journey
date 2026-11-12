
import matplotlib.pyplot as plt

# Student dataset
students = ["Avadhut", "Rahul", "Amit", "Sneha", "Priya"]
marks = [85, 72, 90, 95, 65]

# Create dashboard
plt.figure(figsize=(12, 8))

# Bar Chart
plt.subplot(2, 2, 1)
plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=30)

# Line Chart
plt.subplot(2, 2, 2)
plt.plot(students, marks, marker="o")
plt.title("Marks Progress")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=30)

# Pie Chart
plt.subplot(2, 2, 3)
plt.pie(marks, labels=students, autopct="%1.1f%%")
plt.title("Marks Distribution")

# Scatter Plot
plt.subplot(2, 2, 4)
plt.scatter(students, marks)
plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=30)

plt.tight_layout()

# Save dashboard
plt.savefig("student_dashboard.png")

plt.show()

print("Day 28 Completed!")
