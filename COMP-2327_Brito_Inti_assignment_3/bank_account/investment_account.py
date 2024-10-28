"""
Description: InvestmentAccount class implementing Strategy Pattern for service charges.
Author: Inti Brito Diaz
Date: 2024-10-27
"""

from .bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy
from datetime import date

class InvestmentAccount(BankAccount):
    def __init__(self, account_number: str, balance: float, open_date: date):
        super().__init__(account_number, balance)
        self._open_date = open_date
        self._service_charge_strategy = ManagementFeeStrategy(management_fee=10.00, account_open_date=open_date)

    def get_service_charges(self) -> float:
        return self._service_charge_strategy.calculate_service_charges(self.balance)

    def withdraw(self, amount: float) -> None:
        self.update_balance(-amount)

    def deposit(self, amount: float) -> None:
        self.update_balance(amount)

    def __str__(self) -> str:
        return f"Investment Account {self.account_number}: Balance ${self.balance:.2f}"