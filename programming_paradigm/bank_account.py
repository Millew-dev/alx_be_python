# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        """Adds money to the account balance."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraws money if sufficient balance exists."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Prints the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
