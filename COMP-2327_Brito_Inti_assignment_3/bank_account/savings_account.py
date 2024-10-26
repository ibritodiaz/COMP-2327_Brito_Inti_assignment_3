from datetime import date
from bank_account.bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number: str, balance: float, interest_rate: float, open_date: date):
        super().__init__(account_number, balance)  
        self.interest_rate = interest_rate  
        self.open_date = open_date  

    def get_balance(self):
        return self._balance  

    def withdraw(self, amount):
        self.update_balance(-amount)  
        self._balance -= self.interest_rate * amount

    def deposit(self, amount):
        self.update_balance(amount)  
        self._balance += self.interest_rate * amount

    def __str__(self):
        return f"{self.account_number}: {self._balance:.2f}"

