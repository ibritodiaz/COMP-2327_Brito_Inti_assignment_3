import unittest
from datetime import date
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        class ConcreteBankAccount(BankAccount):
            def get_balance(self):
                return self.balance

        self.BankAccount = ConcreteBankAccount

    def test_init(self):
        account = self.BankAccount("123456", 1000, 0.01, date.today())
        self.assertEqual(account.account_number, "123456")
        self.assertEqual(account.balance, 1000)
        self.assertEqual(account.interest_rate, 0.01)
        self.assertEqual(account.open_date, date.today())
        self.assertEqual(account.get_balance(), 1000)

    def test_deposit(self):
        account = self.BankAccount("123456", 1000, 0.01, date.today())
        account.deposit(500)
        self.assertEqual(account.get_balance(), 1500)

    def test_withdraw(self):
        account = self.BankAccount("123456", 1000, 0.01, date.today())
        account.withdraw(500)
        self.assertEqual(account.get_balance(), 500)

    def test_get_balance(self):
        account = self.BankAccount("123456", 1000, 0.01, date.today())
        self.assertEqual(account.get_balance(), 1000)

    def test_str(self):
        account = self.BankAccount("123456", 1000, 0.01, date.today())
        self.assertEqual(str(account), "123456: 1000.00")

if __name__ == "__main__":
    unittest.main()