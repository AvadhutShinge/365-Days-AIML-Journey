
i = 1

while i <= 10:
    print(i)
    i += 1

# Example 2: Number guessing game
secret_number = 7

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret_number:
        print("Correct! You won!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
