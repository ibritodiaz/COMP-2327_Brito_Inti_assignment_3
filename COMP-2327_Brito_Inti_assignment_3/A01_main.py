"""
Description: A client program written to verify correctness of 
the BankAccount and Transaction classes, including Observer pattern implementation.
Author: ACE Faculty
Edited by: Inti Brito Diaz
Date: 2024-10-27
"""
from bank_account.chequing_account import ChequingAccount
from client.client import Client

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Transaction classes, including Observer pattern.
    """ 
    # 1. Create a valid instance of the Client class.
    try:
        client = Client(10001, "John", "Doe")
        print("Client created successfully.")
    except ValueError as e:
        print(f"Error creating client: {e}")

    # 2. Declare a BankAccount object with an initial value of None.
    bank_account = None

    # 3. Instantiate the ChequingAccount object
    try:
        bank_account = ChequingAccount("20001", 1000.00, 500.00)  # account_number, initial balance, overdraft limit
        print(f"Bank account created successfully. Initial balance: ${bank_account.balance:.2f}")
    except ValueError as e:
        print(f"Error creating bank account: {e}")

    # 4. Attach the client as an observer to the bank account
    bank_account.attach(client)
    print("Client attached as observer to the bank account.")

    # 5. Print the Client instance and the BankAccount instance.
    print("\nClient details:")
    print(client)
    print("\nBank account details:")
    print(bank_account)

    # 6. Attempt to deposit a valid amount.
    try:
        bank_account.deposit(500)
        print(f"Deposit of $500 successful. New balance: ${bank_account.balance:.2f}")
    except ValueError as e:
        print(f"Error depositing: {e}")

    # 7. Attempt to withdraw a valid amount (large transaction).
    try:
        bank_account.withdraw(1200)  # This should trigger a large transaction notification
        print(f"Withdrawal of $1200 successful. New balance: ${bank_account.balance:.2f}")
    except ValueError as e:
        print(f"Error withdrawing: {e}")

    # 8. Attempt to withdraw an amount that will result in a low balance.
    try:
        bank_account.withdraw(bank_account.balance - 50)  # This should trigger a low balance notification
        print(f"Withdrawal successful. New balance: ${bank_account.balance:.2f}")
    except ValueError as e:
        print(f"Error withdrawing: {e}")

    # 9. Print the final state of the BankAccount instance.
    print("\nFinal bank account details:")
    print(bank_account)

if __name__ == "__main__":
    main()