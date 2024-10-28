"""
Description: Abstract base class for service charge calculation strategies.
Author: Inti Brito Diaz
Date: 2024-10-21
"""

from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    BASE_SERVICE_CHARGE = 5.00

    @abstractmethod
    def calculate_service_charges(self, balance: float) -> float:
        pass