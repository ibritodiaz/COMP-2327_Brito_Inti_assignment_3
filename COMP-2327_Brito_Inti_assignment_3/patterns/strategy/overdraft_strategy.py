"""
Description: Strategy for calculating service charges with overdraft fees.
Author: Inti Brito Diaz
Date: 2024-10-21
"""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    def __init__(self, overdraft_fee: float):
        self._overdraft_fee = overdraft_fee

    def calculate_service_charges(self, balance: float) -> float:
        if balance < 0:
            return self.BASE_SERVICE_CHARGE + self._overdraft_fee
        return self.BASE_SERVICE_CHARGE