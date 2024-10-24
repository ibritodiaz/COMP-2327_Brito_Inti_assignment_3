from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    def __init__(self, overdraft_fee: float):
        self.overdraft_fee = overdraft_fee 

    def calculate_service_charges(self, balance: float) -> float:
        if balance < 0:
            return self.BASE_SERVICE_CHARGE + self.overdraft_fee
        return self.BASE_SERVICE_CHARGE
    
    