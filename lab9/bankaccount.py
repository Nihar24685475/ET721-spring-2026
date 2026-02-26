"""
Nihar patel
lab 9, unit testing
Feb 26,2026
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds for this withdrawal!")

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")

        self.balance -= amount

    def get_balance(self):
        return self.balance
