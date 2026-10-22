
student = {
    "name": "Avadhut",
    "age": 21,
    "branch": "AIML",
    "college": "DY Patil University"
}

print("Student Information")
print("Name:", student["name"])
print("Age:", student["age"])
print("Branch:", student["branch"])
print("College:", student["college"])

# Add a new value
student["year"] = 3

# Update a value
student["age"] = 22

print("\nUpdated Student Information:")
for key, value in student.items():
    print(key, ":", value)