
from abc import ABC, abstractmethod


# Abstract Parent Class
class Bank(ABC):

    @abstractmethod
    def calculate_interest(self):
        pass


# Child Class
class SavingsAccount(Bank):

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance!")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful!")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print("Withdrawal successful!")

    def calculate_interest(self):
        return self.__balance * 0.05


# Main Program
print("===== SECURE BANKING SYSTEM =====")

name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

if balance < 0:
    print("Initial balance cannot be negative!")
else:
    account = SavingsAccount(name, balance)

    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Calculate Interest")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Account Holder:", account.name)
            print("Balance:", account.get_balance())

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == "4":
            print("Interest:", account.calculate_interest())

        elif choice == "5":
            print("Thank you for using our banking system!")
            break

        else:
            print("Invalid choice!")
