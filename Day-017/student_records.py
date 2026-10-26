
print("===== STUDENT RECORD MANAGER =====")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
marks = input("Enter marks: ")

# Save student details to a file
with open("Day-017/students.txt", "a") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Roll Number: {roll_no}\n")
    file.write(f"Marks: {marks}\n")
    file.write("--------------------\n")

print("\nStudent record saved successfully!")

# Read and display student records
with open("Day-017/students.txt", "r") as file:
    print("\n===== SAVED STUDENT RECORDS =====")
    print(file.read())
