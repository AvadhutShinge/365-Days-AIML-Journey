

def factorial_loop(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)


number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Please enter a non-negative integer.")
elif number > 900:
    print("Please enter a number between 0 and 900.")
else:
    print("Factorial using loop:", factorial_loop(number))
    print("Factorial using recursion:", factorial_recursive(number))
