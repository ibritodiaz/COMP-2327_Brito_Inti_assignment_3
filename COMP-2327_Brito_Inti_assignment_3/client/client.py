"""
Description: Client class implementing Observer pattern.
Author: Inti Brito Diaz
Date: 2024-10-27
"""

from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import datetime

class Client(Observer):
    def __init__(self, client_number: int, first_name: str, last_name: str):
        self.client_number = client_number
        self.first_name = first_name
        self.last_name = last_name

    def update(self, message: str):
        subject = f"ALERT: Unusual Activity: {datetime.now()}"
        full_message = f"Notification for {self.client_number}: {self.first_name} {self.last_name}: {message}"
        email_address = f"{self.client_number}@example.com"  # Creating a dummy email address
        simulate_send_email(email_address, subject, full_message)

    def __str__(self):
        return f"Client {self.client_number}: {self.first_name} {self.last_name}"