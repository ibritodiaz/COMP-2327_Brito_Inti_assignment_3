"""
Description: Test cases for the InvestmentAccount class.
Author: Inti Brito Diaz
Date: 2024-10-27
"""

import unittest
from datetime import date
from bank_account.investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):
    def setUp(self):
        self.account = InvestmentAccount("123456", 1000, date.today())

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_withdraw(self):
        self.account.withdraw(500)
        self.assertEqual(self.account.balance, 500)

    def test_get_balance(self):
        self.assertEqual(self.account.balance, 1000)

    def test_get_service_charges(self):
        charges = self.account.get_service_charges()
        self.assertIsInstance(charges, float)

    def test_str(self):
        expected_str = "Investment Account 123456: Balance $1000.00"
        self.assertEqual(str(self.account), expected_str)

if __name__ == '__main__':
    unittest.main()