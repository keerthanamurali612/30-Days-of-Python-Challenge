'''
Create a Python class representing a simple bank account.
The account should have the following attributes and methods

Attributes:

account_number (a string, unique for each account)
account_holder (a string, representing the name of the account holder)
balance (a float, representing the current balance in the account)
'''



class bank_account:
    def __init__(self,account_number,account_holder,initial_balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=initial_balance
    def deposit(self,amount):
        self.balance +=amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal canceled.")
    def get_balance(self):
        return self.balance


bank1=bank_account(1232187289,"rudra",1000.0)
bank1.deposit(500.0)
bank1.withdraw(200.0)
bank1.withdraw(2000.0)  # This should print an insufficient funds message
bank1.deposit(300.0)


print(f"\nFinal Account Details:")
print(f"Account Holder: {bank1.account_holder}")
print(f"Account Number: {bank1.account_number}")
print(f"Final Balance: ${bank1.get_balance()}")
