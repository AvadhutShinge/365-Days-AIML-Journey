
print("===== SAFE CALCULATOR =====")

try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        raise ValueError("Invalid operator!")

except ValueError as e:
    print("Input error:", e)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

else:
    print("Result:", result)

finally:
    print("Calculator program finished.")
