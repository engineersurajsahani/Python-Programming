# Bank account class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def check_balance(self):
        return self.balance

account = BankAccount()
account.deposit(1000)
account.withdraw(500)
print(account.check_balance())
