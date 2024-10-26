import unittest
from datetime import datetime
from bank_account.savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):
    def setUp(self):
        self.account = SavingsAccount("123456", 1000, 0.01, datetime.now())

    def test_str(self):
        self.assertEqual(str(self.account), "123456: 1000.00")

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_withdraw(self):
        self.account.withdraw(500)
        self.assertEqual(self.account.get_balance(), 495)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1505)

if __name__ == '__main__':
    unittest.main()