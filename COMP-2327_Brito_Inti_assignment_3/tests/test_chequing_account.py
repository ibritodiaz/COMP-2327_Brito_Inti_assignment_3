import unittest
from datetime import datetime
from bank_account.chequing_account import ChequingAccount

class TestChequingAccount(unittest.TestCase):
    def test_get_balance(self):
        account = ChequingAccount("123456", 1000, 0.01, datetime.now(), 10)
        self.assertEqual(account.get_balance(), 990)

    def test_withdraw(self):
        account = ChequingAccount("123456", 1000, 0.01, datetime.now(), 10)
        account.withdraw(500)
        self.assertEqual(account.get_balance(), 480)

    def test_deposit(self):
        account = ChequingAccount("123456", 1000, 0.01, datetime.now(), 10)
        account.deposit(500)
        self.assertEqual(account.get_balance(), 1480)

    def test_str(self):
        account = ChequingAccount("123456", 1000, 0.01, datetime.now(), 10)
        self.assertEqual(str(account), "123456: 990.00")

if __name__ == '__main__':
    unittest.main()