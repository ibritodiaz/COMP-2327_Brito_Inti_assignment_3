"""
Description: Abstract base class for bank accounts implementing Subject and Strategy patterns.
This class provides the framework for the Observer pattern (for notifications) and
the Strategy pattern (for service charge calculations).
Author: Inti Brito Diaz
Date: 2024-10-27
"""

from patterns.observer.subject import Subject
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from abc import ABC, abstractmethod

class BankAccount(Subject, ABC):
    LOW_BALANCE_LEVEL = 100.00
    LARGE_TRANSACTION_THRESHOLD = 5000.00

    def __init__(self, account_number: str, balance: float):
        super().__init__()
        self._balance = balance
        self.account_number = account_number
        self._service_charge_strategy = None  # This will be set by subclasses

    @property
    def balance(self):
        return self._balance

    def update_balance(self, amount: float):
        print(f"Updating balance for account {self.account_number}")
        print(f"Current balance: ${self._balance:.2f}")
        print(f"Transaction amount: ${amount:.2f}")
        
        self._balance += amount
        print(f"New balance: ${self._balance:.2f}")

        if self._balance < self.LOW_BALANCE_LEVEL:
            print(f"Low balance warning for account {self.account_number}")
            self.notify(f"Low balance warning ${self._balance:.2f}: on account {self.account_number}.")
        
        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            print(f"Large transaction alert for account {self.account_number}")
            self.notify(f"Large transaction ${abs(amount):.2f}: on account {self.account_number}.")

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    @abstractmethod
    def deposit(self, amount: float):
        pass

    def get_service_charges(self) -> float:
        if self._service_charge_strategy is None:
            raise NotImplementedError("Service charge strategy not set")
        return self._service_charge_strategy.calculate_service_charges(self.balance)

    def set_service_charge_strategy(self, strategy: ServiceChargeStrategy):
        self._service_charge_strategy = strategy

    def __str__(self):
        return f"Account {self.account_number}: Balance ${self._balance:.2f}"