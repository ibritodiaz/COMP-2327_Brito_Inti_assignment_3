"""
Description: Test cases for the SavingsAccount class.
Author: Inti Brito Diaz
Date: 2024-10-27
"""

import unittest
from bank_account.savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):
    def setUp(self):
        self.account = SavingsAccount("123456", 1000, 0.01)

    def test_str(self):
        expected_str = "Savings Account 123456: Balance $1000.00"
        self.assertEqual(str(self.account), expected_str)

    def test_get_balance(self):
        self.assertEqual(self.account.balance, 1000)

    def test_withdraw(self):
        self.account.withdraw(500)
        self.assertEqual(self.account.balance, 500)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_get_service_charges(self):
        # Test for account above minimum balance
        self.assertEqual(self.account.get_service_charges(), 5.00)  # BASE_SERVICE_CHARGE

        # Test for account below minimum balance
        low_balance_account = SavingsAccount("789012", 50, 0.01)
        self.assertEqual(low_balance_account.get_service_charges(), 10.00)  # BASE_SERVICE_CHARGE + min_balance_fee

if __name__ == '__main__':
    unittest.main()