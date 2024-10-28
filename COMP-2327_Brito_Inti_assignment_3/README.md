# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments. Each 
assignment will build on the work done in the previous assignment(s). Ultimately, 
an entire system will be created to manage bank transactions for clients who 
have one or more bank accounts.

## Author
Inti Brito Diaz

## Assignment
Assignment 1: Classes, Encapsulation and Unit Test Planning

This assignment focused on developing foundational classes for a larger banking system, incorporating encapsulation through private attributes and public accessors/mutators. It also included unit test planning for these classes.

Assignment 2: Abstraction, Inheritance and Polymorphism

This assignment built upon the previous work by implementing abstract classes, inheritance relationships between different account types, and polymorphic behavior in service charge calculations. We created subclasses for different account types (Chequing, Savings, Investment) that inherit from a common BankAccount class.

Assignment 3: Applying Design Patterns

In this assignment, we're addressing issues related to the scalability and maintainability of the service charge calculation functionality. We're applying the Strategy Pattern to simplify and add scalability to the service charge functionality. Additionally, we're introducing the Observer Pattern to notify clients of large transactions and low balance situations.

## Encapsulation
Encapsulation was achieved in the BankAccount and Transaction classes by using private attributes (denoted with an underscore prefix in Python) and providing public methods to access and modify these attributes when necessary. This approach helps to maintain data integrity and provides a clear interface for interacting with the objects.

## Polymorphism
Polymorphism is implemented through the get_service_charges() method in the BankAccount subclasses. Each account type (Chequing, Savings, Investment) has its own implementation of this method, allowing for different service charge calculations based on the specific account rules. This means we can treat all accounts the same way when calculating service charges, but each type will behave differently based on its own logic.

## Design Patterns
### Strategy Pattern
The Strategy Pattern is being implemented to make the service charge calculations more flexible and scalable. This allows us to easily add new account types with different charge calculations without modifying existing code.

### Observer Pattern
The Observer Pattern is being used to notify clients about significant events such as large transactions and low balance situations. This keeps the client informed without tightly coupling the account and client code.

## Challenges and Learning
[This section can be filled with your personal reflections on the challenges you faced and what you learned during the assignment.]

## Next Steps
[You can use this section to outline future improvements or features you'd like to add to the project.]