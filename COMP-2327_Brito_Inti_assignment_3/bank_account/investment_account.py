from bank_account import BankAccount
from datetime import datetime, timedelta

class InvestmentAccount(BankAccount):
    TWENTY_YEARS_AGO = datetime.now() - timedelta(days=365*20)

    def __init__(self, account_number: str, balance: float, interest_rate, open_date: datetime):
        super().__init__(account_number, balance, interest_rate, open_date)

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        super().withdraw(amount)

    def deposit(self, amount):
        super().deposit(amount)

    def __str__(self):
        return f"{self.account_number}: {self.balance:.2f}"