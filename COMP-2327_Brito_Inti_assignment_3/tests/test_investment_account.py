import unittest
from datetime import datetime
from bank_account.investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):
    def test_get_balance(self):
        account = InvestmentAccount("123456", 1000, 0.01, datetime.now())
        self.assertEqual(account.get_balance(), 1000)

    def test_withdraw(self):
        account = InvestmentAccount("123456", 1000, 0.01, datetime.now())
        account.withdraw(500)
        self.assertEqual(account.get_balance(), 500)

    def test_deposit(self):
        account = InvestmentAccount("123456", 1000, 0.01, datetime.now())
        account.deposit(500)
        self.assertEqual(account.get_balance(), 1500)

    def test_str(self):
        account = InvestmentAccount("123456", 1000, 0.01, datetime.now())
        self.assertEqual(str(account), "123456: 1000.00")

if __name__ == '__main__':
    unittest.main()