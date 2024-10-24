
from datetime import date, timedelta
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class ManagementFeeStrategy(ServiceChargeStrategy):
    TEN_YEARS_AGO = date.today() - timedelta(days=365*10)

    def __init__(self, management_fee: float):
        self.management_fee = management_fee

    def calculate_service_charges(self, balance: float) -> float:
        return self.BASE_SERVICE_CHARGE + self.management_fee
    
