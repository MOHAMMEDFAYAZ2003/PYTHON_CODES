# without magic method __str__()
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
s1=Student('pradeep',12)
s2=Student('Ravi',13)
print(s1)   #it prints address of object reference   
print(s2)
print(s1.name)
print(s2.rollno)

# magic method __str__()
class Student:
    
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        
    def __str__(self):
        return"The student name is {} and marks {}.".format(self.name,self.roll)
    
s1=Student('Pradeep',11)
s2=Student('Shiva',22)
print(s1)
print(s2)
        
import datetime
today=datetime.datetime.now()
print (today)
print(type(today))
s=repr(today)  #conveting datetime object to str
print(type(s))
d=eval(s)      #converting datetime str to object 
print(type(d))
print(d)


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


 
