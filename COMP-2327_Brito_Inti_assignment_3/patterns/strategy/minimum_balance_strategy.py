from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Strategy for calculating service charges based on a minimum balance requirement.
    """
    def __init__(self, min_balance_fee: float, minimum_balance: float):
        self._min_balance_fee = min_balance_fee
        self._minimum_balance = minimum_balance

    def calculate_service_charges(self, balance: float) -> float:
        """
        Calculate service charges based on account balance.

        Args:
            balance (float): The current account balance.

        Returns:
            float: The calculated service charge.
        """
        if balance < self._minimum_balance:
            return self.BASE_SERVICE_CHARGE + self._min_balance_fee
        return self.BASE_SERVICE_CHARGE