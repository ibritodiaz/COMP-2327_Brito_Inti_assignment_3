try:
    print("Starting the program...")

    """
    Description: A client program written to verify implementation 
    of the Observer Pattern.
    Author: ACE Faculty
    Edited by: Inti Brito Diaz
    Date: 2024-10-21
    """

    # 1.  Import all BankAccount types using the bank_account package
    #     Import date
    #     Import Client
    from bank_account.chequing_account import ChequingAccount
    from bank_account.savings_account import SavingsAccount
    from client.client import Client
    from datetime import date

    # 2. Create a Client object with data of your choice.
    client1 = Client(client_number=1001, first_name="John", last_name="Doe")
    print(f"Created client1: {client1}")

    # 3a. Create a ChequingAccount object with data of your choice, using the client_number 
    # of the client created in step 2.
    chequing_account = ChequingAccount(account_number=5001, balance=2000)
    print(f"Created chequing_account: {chequing_account}")

    # 3b. Create a SavingsAccount object with data of your choice, using the client_number 
    # of the client created in step 2.
    savings_account = SavingsAccount(account_number=6001, balance=1500, interest_rate=0.02, open_date=date.today())
    print(f"Created savings_account: {savings_account}")

    # 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
    # The Client object is an 'Observer' object.  
    # 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 3a).
    chequing_account.attach(client1)
    print("Attached client1 to chequing_account")

    # 4b.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 3b).
    savings_account.attach(client1)
    print("Attached client1 to savings_account")

    # 5a. Create a second Client object with data of your choice.
    client2 = Client(client_number=1002, first_name="Jane", last_name="Smith")
    print(f"Created client2: {client2}")

    # 5b. Create a SavingsAccount object with data of your choice, using the client_number 
    # of the client created in this step.
    savings_account_2 = SavingsAccount(account_number=6002, balance=2500, interest_rate=0.02, open_date=date.today())
    print(f"Created savings_account_2: {savings_account_2}")

    # Attach the second client to their own savings account
    savings_account_2.attach(client2)
    print("Attached client2 to savings_account_2")

    # 6. Use the ChequingAccount and SavingsAccount objects created 
    # in steps 3 and 5 above to perform transactions (deposits and withdraws) 
    # which would cause the Subject (BankAccount) to notify the Observer 
    # (Client) as well as transactions that would not 
    # cause the Subject to notify the Observer.  Ensure each 
    # BankAccount object performs at least 3 transactions.
    # REMINDER: the deposit() and withdraw() methods can raise exceptions
    # ensure the methods are invoked using proper exception handling such 
    # that any exception messages are printed to the console.

    # Perform transactions with exception handling
    try:
        # Transactions on ChequingAccount (Client 1)
        print("\nPerforming transactions on ChequingAccount (Client 1):")
        chequing_account.update_balance(-2100)  # Withdraw below balance (should trigger notification for low balance)
        chequing_account.update_balance(5000)   # Deposit large amount (should trigger notification)
        chequing_account.update_balance(-100)   # Small transaction (no notification)
    except Exception as e:
        print(f"Error with ChequingAccount transactions: {e}")

    try:
        # Transactions on SavingsAccount (Client 1)
        print("\nPerforming transactions on SavingsAccount (Client 1):")
        savings_account.update_balance(-1600)  # Withdraw causing low balance (should trigger notification)
        savings_account.update_balance(5000)   # Deposit large amount (should trigger notification)
        savings_account.update_balance(50)     # Small transaction (no notification)
    except Exception as e:
        print(f"Error with SavingsAccount transactions: {e}")

    try:
        # Transactions on SavingsAccount 2 (Client 2)
        print("\nPerforming transactions on SavingsAccount 2 (Client 2):")
        savings_account_2.update_balance(-2600)  # Withdraw below balance (should trigger notification for low balance)
        savings_account_2.update_balance(6000)   # Deposit large amount (should trigger notification)
        savings_account_2.update_balance(-50)    # Small transaction (no notification)
    except Exception as e:
        print(f"Error with SavingsAccount 2 transactions: {e}")

    print("Program finished.")
except Exception as e:
    print(f"An error occurred: {e}")