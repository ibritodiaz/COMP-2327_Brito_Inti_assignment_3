"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
Author: ACE Faculty
Edited by: Inti Brito Diaz
Date: 2024-09-30
"""

from bank_account import ChequingAccount, SavingsAccount, InvestmentAccount
from datetime import date, timedelta

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing = ChequingAccount("123456", 900, 0.01, date.today(), 10)

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(chequing)
print(f"Service charges: ${chequing.get_service_charges():.2f}")

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
chequing.deposit(1000)
print(chequing)
print(f"Service charges: ${chequing.get_service_charges():.2f}")

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
savings = SavingsAccount("234567", 1000, 0.02, date.today())

# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(savings)
print(f"Service charges: ${savings.get_service_charges():.2f}")

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
savings.withdraw(900)
print(savings)
print(f"Service charges: ${savings.get_service_charges():.2f}")

print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
investment_new = InvestmentAccount("345678", 1000, 0.03, date.today() - timedelta(days=365*5))

# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(investment_new)
print(f"Service charges: ${investment_new.get_service_charges():.2f}")

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
investment_old = InvestmentAccount("456789", 1000, 0.03, date.today() - timedelta(days=365*15))

# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(investment_old)
print(f"Service charges: ${investment_old.get_service_charges():.2f}")

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
chequing.withdraw(chequing.get_service_charges())
savings.withdraw(savings.get_service_charges())
investment_new.withdraw(investment_new.get_service_charges())
investment_old.withdraw(investment_old.get_service_charges())

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print(chequing)
print(savings)
print(investment_new)
print(investment_old)