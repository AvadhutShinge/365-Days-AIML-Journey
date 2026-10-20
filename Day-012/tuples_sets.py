
# Day 12: Python Tuples and Sets

# 1. Tuple example
student = ("Avadhut", 21, "AIML")

print("Student Details:")
print("Name:", student[0])
print("Age:", student[1])
print("Branch:", student[2])

# 2. Set example: Remove duplicates
marks = [80, 90, 80, 75, 90, 85]
unique_marks = set(marks)

print("\nOriginal Marks:", marks)
print("Unique Marks:", unique_marks)

# 3. Set operations
python_students = {"Amit", "Rahul", "Sneha"}
aiml_students = {"Sneha", "Priya", "Amit"}

print("\nPython Students:", python_students)
print("AIML Students:", aiml_students)
print("Students in both groups:", python_students & aiml_students)
print("All students:", python_students | aiml_students)
print("Only Python group:", python_students - aiml_students)
