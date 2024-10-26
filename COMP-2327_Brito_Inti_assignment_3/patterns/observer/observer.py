
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message: str):

        """
        Abstract method to be implemented by concrete observers to receive updates from the Subject.
        """
        pass

    