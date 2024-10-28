"""
Description: ChequingAccount class implementing Strategy Pattern for service charges.
Author: Inti Brito Diaz
Date: 2024-10-27
"""

from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    def __init__(self, account_number: str, balance: float, overdraft_limit: float):
        super().__init__(account_number, balance)
        self._overdraft_limit = overdraft_limit
        self._service_charge_strategy = OverdraftStrategy(overdraft_fee=35.00)

    def get_service_charges(self) -> float:
        return self._service_charge_strategy.calculate_service_charges(self.balance)

    def deposit(self, amount: float) -> None:
        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        if self.balance - amount < -self._overdraft_limit:
            raise ValueError("Withdrawal amount exceeds overdraft limit")
        self.update_balance(-amount)

    def __str__(self) -> str:
        return f"Chequing Account {self.account_number}: Balance ${self.balance:.2f}"