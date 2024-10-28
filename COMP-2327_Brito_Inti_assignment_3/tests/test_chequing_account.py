"""
Description: Unit tests for BankAccount class.
Author: Inti Brito Diaz
Date: 2024-10-21
"""

import unittest
from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class TestServiceChargeStrategy(ServiceChargeStrategy):
    def calculate_service_charges(self, balance: float) -> float:
        return self.BASE_SERVICE_CHARGE

class ConcreteBankAccount(BankAccount):
    def __init__(self, account_number: str, balance: float):
        super().__init__(account_number, balance)
        self._service_charge_strategy = TestServiceChargeStrategy()

    def withdraw(self, amount: float):
        self.update_balance(-amount)

    def deposit(self, amount: float):
        self.update_balance(amount)

    def get_service_charges(self) -> float:
        return self._service_charge_strategy.calculate_service_charges(self.balance)

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.BankAccount = ConcreteBankAccount

    def test_init(self):
        account = self.BankAccount("123456", 1000)
        self.assertEqual(account.account_number, "123456")
        self.assertEqual(account.balance, 1000)

    def test_deposit(self):
        account = self.BankAccount("123456", 1000)
        account.deposit(500)
        self.assertEqual(account.balance, 1500)

    def test_withdraw(self):
        account = self.BankAccount("123456", 1000)
        account.withdraw(500)
        self.assertEqual(account.balance, 500)

    def test_get_balance(self):
        account = self.BankAccount("123456", 1000)
        self.assertEqual(account.balance, 1000)

    def test_str(self):
        account = self.BankAccount("123456", 1000)
        self.assertEqual(str(account), "Account 123456: Balance $1000.00")

    def test_get_service_charges(self):
        account = self.BankAccount("123456", 1000)
        self.assertEqual(account.get_service_charges(), ServiceChargeStrategy.BASE_SERVICE_CHARGE)

if __name__ == "__main__":
    unittest.main()