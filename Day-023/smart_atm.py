# Custom Exception Classes

class InvalidAmountError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


# ATM Class

class SmartATM:

    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print("Available Balance:", self.balance)

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero!")

        self.balance += amount
        print("Money deposited successfully!")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Enter a valid amount!")

        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance!")

        self.balance -= amount
        print("Withdrawal successful!")


# Main Program

atm = SmartATM(5000)

while True:
    print("\n===== SMART ATM SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            atm.check_balance()

        elif choice == 2:
            amount = float(input("Enter deposit amount: "))
            atm.deposit(amount)

        elif choice == 3:
            amount = float(input("Enter withdrawal amount: "))
            atm.withdraw(amount)

        elif choice == 4:
            print("Thank you for using Smart ATM!")
            break

        else:
            print("Invalid choice! Please try again.")

    except InvalidAmountError as e:
        print("Error:", e)

    except InsufficientBalanceError as e:
        print("Error:", e)

    except ValueError:
        print("Please enter a valid number!")