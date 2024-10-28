# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments. Each 
assignment will build on the work done in the previous assignment(s). Ultimately, 
an entire system will be created to manage bank transactions for clients who 
have one or more bank accounts.

## Author
Inti Brito Diaz

## Assignment Overview

### Assignment 1: Classes, Encapsulation and Unit Test Planning
This assignment focused on developing foundational classes for a larger banking system, incorporating encapsulation through private attributes and public accessors/mutators. It also included unit test planning for these classes.

### Assignment 2: Abstraction, Inheritance and Polymorphism
This assignment built upon the previous work by implementing abstract classes, inheritance relationships between different account types, and polymorphic behavior in service charge calculations. We created subclasses for different account types (Chequing, Savings, Investment) that inherit from a common BankAccount class.

### Assignment 3: Applying Design Patterns
In this assignment, we're addressing issues related to the scalability and maintainability of the service charge calculation functionality. We're applying the Strategy Pattern to simplify and add scalability to the service charge functionality. Additionally, we're introducing the Observer Pattern to notify clients of large transactions and low balance situations.

## Encapsulation
Encapsulation was achieved in the BankAccount and Transaction classes by using private attributes (denoted with an underscore prefix in Python) and providing public methods to access and modify these attributes when necessary. This approach helps maintain data integrity and provides a clear interface for interacting with the objects.

## Polymorphism
Polymorphism is implemented through the `get_service_charges()` method in the BankAccount subclasses. Each account type (Chequing, Savings, Investment) has its own implementation of this method, allowing for different service charge calculations based on specific account rules. This means we can treat all accounts the same way when calculating service charges, but each type will behave differently based on its own logic.

## Design Patterns

### Strategy Pattern
The Strategy Pattern is being implemented to make service charge calculations more flexible and scalable. This allows us to easily add new account types with different charge calculations without modifying existing code.

### Observer Pattern
The Observer Pattern is being used to notify clients about significant events such as large transactions and low balance situations. This keeps clients informed without tightly coupling the account and client code.

## Challenges and Learning
Throughout this assignment, I faced several challenges that helped deepen my understanding of design patterns in Python:

- **Implementing the Strategy Pattern**: Initially, I struggled with where to place the calculation logic. After some trial and error, I realized how important it is to separate concerns.
  
- **Understanding the Observer Pattern**: This was new territory for me. I had to wrap my head around how observers are notified without being tightly coupled to their subjects.
  
- **Testing**: Writing unit tests for each account type was tedious but rewarding. It helped me catch bugs I wouldn't have noticed otherwise.

## Next Steps
Looking ahead, I plan to:

- Fix any remaining issues with the SavingsAccount and InvestmentAccount tests.
- Add more diverse transactions in `A03_main.py` to showcase the Observer pattern in action.
- Explore additional features like allowing clients to customize their notification preferences.
  
This project has been a valuable learning experience, pushing me to think critically about code design while applying what I've learned about Python programming.