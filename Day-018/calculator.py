
import operations

print("===== MODULAR CALCULATOR =====")

a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if operator == "+":
    result = operations.add(a, b)
elif operator == "-":
    result = operations.subtract(a, b)
elif operator == "*":
    result = operations.multiply(a, b)
elif operator == "/":
    result = operations.divide(a, b)
else:
    result = "Invalid operator"

print("Result:", result)
