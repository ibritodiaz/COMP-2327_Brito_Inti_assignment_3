from bank_account.bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy
from datetime import date

class SavingsAccount(BankAccount):
    def __init__(self, account_number: str, balance: float, interest_rate: float):
        super().__init__(account_number, balance)
        self._interest_rate = interest_rate
        self._service_charge_strategy = MinimumBalanceStrategy(min_balance_fee=5.00, minimum_balance=100.00)

    def get_service_charges(self) -> float:
        return self._service_charge_strategy.calculate_service_charges(self.balance)

    def deposit(self, amount: float) -> None:
        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        self.update_balance(-amount)

    def __str__(self) -> str:
        return f"Savings Account {self.account_number}: Balance ${self.balance:.2f}"