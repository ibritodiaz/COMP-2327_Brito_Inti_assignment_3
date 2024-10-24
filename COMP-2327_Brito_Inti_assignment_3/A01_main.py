"""
Description: A client program written to verify correctness of 
the BankAccount and Transaction classes.
Author: ACE Faculty
Edited by: Inti Brito Diaz
Date: 2024-09-09
"""
from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Transaction classes.
    """ 
    # 1. Create a valid instance of the Client class.
    try:
        client = Client(10001, "John", "Doe", "jdoe@example.com")
        print("Client created successfully.")
    except ValueError as e:
        print(f"Error creating client: {e}")

    # 2. Declare a BankAccount object with an initial value of None.
    bank_account = None

    # 3. Instantiate the BankAccount object.
    try:
        bank_account = BankAccount(20001, client.client_number, 1000.00)
        print(f"Bank account created successfully. Initial balance: ${bank_account.balance:.2f}")
    except ValueError as e:
        print(f"Error creating bank account: {e}")

    # 4. Create an instance of the BankAccount class with an invalid balance.
    try:
        invalid_account = BankAccount(20002, client.client_number, "invalid_balance")
        print("Invalid bank account created successfully.")
    except ValueError as e:
        print(f"Error creating invalid bank account: {e}")

    # 5. Print the Client instance and the BankAccount instance.
    print("\nClient details:")
    print(client)
    print("\nBank account details:")
    print(bank_account)

    # 6. Attempt to deposit a non-numeric value.
    try:
        bank_account.deposit("invalid_amount")
    except ValueError as e:
        print(f"Error depositing non-numeric value: {e}")

    # 7. Attempt to deposit a negative value.
    try:
        bank_account.deposit(-100)
    except ValueError as e:
        print(f"Error depositing negative value: {e}")

    # 8. Attempt to withdraw a valid amount.
    try:
        bank_account.withdraw(500)
        print(f"Withdrawal of $500 successful. New balance: ${bank_account.balance:.2f}")
    except ValueError as e:
        print(f"Error withdrawing valid amount: {e}")

    # 9. Attempt to withdraw a non-numeric value.
    try:
        bank_account.withdraw("invalid_amount")
    except ValueError as e:
        print(f"Error withdrawing non-numeric value: {e}")

    # 10. Attempt to withdraw a negative value.
    try:
        bank_account.withdraw(-100)
    except ValueError as e:
        print(f"Error withdrawing negative value: {e}")

    # 11. Attempt to withdraw a value exceeding the current balance.
    try:
        bank_account.withdraw(10000)
    except ValueError as e:
        print(f"Error withdrawing amount exceeding balance: {e}")

    # 12. Print the final state of the BankAccount instance.
    print("\nFinal bank account details:")
    print(bank_account)

if __name__ == "__main__":
    main()