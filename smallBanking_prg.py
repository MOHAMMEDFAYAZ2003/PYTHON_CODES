# small banking program-1
import sys
class Customer:
    '''Customer class with bank operations'''
    bank_name = 'SBI'

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient funds....")
            sys.exit()
        self.balance -= amt
        print('Balance after Withdraw:', self.balance)

print("Welcome to", Customer.bank_name)
name = input("Enter your name: ")
print(f"Hey {name} Welcome to SBI")
customer = Customer(name)

while True:
    choice = input("Choose any option Deposit (D),Withdraw (W)Exit (E): ").upper()

    if choice == 'D':
        amt = float(input("Enter the deposit amount: "))
        customer.deposit(amt)
        print("Balance after deposit:", customer.balance)
    elif choice == 'W':
        amt = float(input("Enter the withdrawal amount: "))
        if amt>customer.balance:
            print("Insufficient Balance...")
            sys.exit()
        customer.withdraw(amt)

    elif choice == 'E':
        print("Thanks for banking....")
        sys.exit()
    else:
        print("Invalid option. Please select a valid option...")


# small banking program-2
 # Small Banking app
class Account:
    
    def __init__(self,name,balance,min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance
    
    def deposit(self,amount):
        self.balance+=amount
    
    def withdraw(self,amount):
        if self.balance-amount>=self.min_balance:
            self.balance-=amount
        else:
            print("Sorry insuficient funds...!")
    
    def print_stm(self):
        print('Your balance is {}'.format(self.balance))
            
            
class Current(Account):
    
    def __init__ (self,name,balance):
        super().__init__(name,balance,min_balance=1000)
   
    def __str__(self):
        return "{} your currrent account balance is {}.".format(self.name,self.balance)
    
class Savings(Account):
    
    def __init__ (self,name,balance):
        super().__init__(name,balance,min_balance=0)
    
    def __str__(self):
        return "{} your balance is {}".format(self.name,self.balance)
    

c=Savings("Indra",10000)
print(c)
c.deposit(5000)
c.print_stm()
c.withdraw(16000)
c.withdraw(15000)
c.print_stm()
print()

c2=Current("sai",20000)
c2.deposit(1)
c2.print_stm()
c2.withdraw(1000)
c2.print_stm()
c2.withdraw(100000)
print(c2)
