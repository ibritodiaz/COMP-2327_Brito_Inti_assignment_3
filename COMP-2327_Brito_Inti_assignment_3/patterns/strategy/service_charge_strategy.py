
from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    BASE_SERVICE_CHARGE = 5.00

    @abstractmethod
    def calculate_service_charges(self, balance: float) -> float:
        """
        Abstract method to be implemented by subclasses to calculate service charges.
        """
        pass