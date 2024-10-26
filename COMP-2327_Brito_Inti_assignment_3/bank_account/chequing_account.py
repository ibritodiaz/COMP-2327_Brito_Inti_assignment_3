
from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    def __init__(self, account_number: int, balance: float):
        super().__init__(account_number, balance)
        self._service_charge_strategy = OverdraftStrategy(overdraft_fee=35.00)

    def get_service_charges(self) -> float:
        return self._service_charge_strategy.calculate_service_charges(self.get_balance())
    
