"""
Description: Strategy for calculating service charges with management fees.
Author: Inti Brito Diaz
Date: 2024-10-27
"""

from datetime import date, timedelta
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class ManagementFeeStrategy(ServiceChargeStrategy):
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, management_fee: float, account_open_date: date):
        self._management_fee = management_fee
        self._account_open_date = account_open_date

    def calculate_service_charges(self, balance: float) -> float:
        if self._account_open_date > self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE + self._management_fee
        return self.BASE_SERVICE_CHARGE