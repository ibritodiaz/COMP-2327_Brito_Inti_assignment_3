
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    def __init__(self, min_balance_fee: float, minimum_balance: float):
        self.min_balance_fee = min_balance_fee

        self.minimum_balance = minimum_balance

    def calculate_service_charges(self, balance: float) -> float:
        if balance < self.minimum_balance:
            return self.BASE_SERVICE_CHARGE + self.min_balance_fee
        return self.BASE_SERVICE_CHARGE
        