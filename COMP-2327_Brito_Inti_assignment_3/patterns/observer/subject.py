"""
Description: Subject class for the Observer pattern.
Author: Inti Brito Diaz
Date: 2024-10-27
"""

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)