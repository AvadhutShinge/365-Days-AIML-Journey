
# Parent Class
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

    def calculate_bonus(self):
        return self.salary * 0.10


# Child Class 1
class Manager(Employee):

    def calculate_bonus(self):
        return self.salary * 0.20


# Child Class 2
class Developer(Employee):

    def calculate_bonus(self):
        return self.salary * 0.15


# Main Program
print("===== EMPLOYEE MANAGEMENT SYSTEM =====")

name = input("Enter employee name: ")
salary = float(input("Enter employee salary: "))

print("\nSelect Employee Type:")
print("1. Manager")
print("2. Developer")

choice = input("Enter choice: ")

if choice == "1":
    employee = Manager(name, salary)

elif choice == "2":
    employee = Developer(name, salary)

else:
    print("Invalid employee type!")
    exit()

print("\n===== EMPLOYEE DETAILS =====")

employee.display()

print("Bonus:", employee.calculate_bonus())

print("Total Salary:", employee.salary +
      employee.calculate_bonus())
