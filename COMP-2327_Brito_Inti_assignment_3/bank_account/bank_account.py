

from patterns.observer.subject import Subject

class BankAccount(Subject):
    LOW_BALANCE_LEVEL = 100.00
    LARGE_TRANSACTION_THRESHOLD = 5000.00

    def __init__(self, account_number: int, balance: float):
        super().__init__()
        self._balance = balance
        self.account_number = account_number

    def update_balance(self, amount: float):
        self._balance += amount

        
        if self._balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning ${self._balance}: on account {self.account_number}.")
        
        
        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction ${amount}: on account {self.account_number}.")
