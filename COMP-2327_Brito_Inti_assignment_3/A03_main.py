"""
Description: A client program written to verify implementation 
of the Observer Pattern.
Author: ACE Faculty
Edited by: Inti Brito Diaz
Date: 2024-10-27
"""

from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount
from client.client import Client
from datetime import date, timedelta

def main():
    try:
        print("Starting the program...")

        # Create clients
        client1 = Client(1001, "John", "Doe")
        print(f"Created client1: {client1}")
        
        client2 = Client(1002, "Jane", "Smith")
        print(f"Created client2: {client2}")

        # Create bank accounts
        chequing = ChequingAccount("CH001", 1000.00, 500.00)
        savings = SavingsAccount("SV001", 2000.00, 0.02)
        investment = InvestmentAccount("IN001", 5000.00, date.today() - timedelta(days=365*5))

        # Attach clients to accounts
        chequing.attach(client1)
        savings.attach(client1)
        investment.attach(client2)

        # Perform transactions
        print("\nPerforming transactions on ChequingAccount (Client 1):")
        chequing.deposit(6000.00)  # Should trigger large transaction notification
        chequing.withdraw(6500.00)  # Should trigger large transaction and low balance notifications
        
        print("\nPerforming transactions on SavingsAccount (Client 1):")
        savings.withdraw(1950.00)  # Should trigger low balance notification
        
        print("\nPerforming transactions on InvestmentAccount (Client 2):")
        investment.withdraw(4900.00)  # Should trigger low balance notification

        print("Program completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()