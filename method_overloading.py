class M_overloading:
    def m1(self):
        print("No argument")
    def m1(self,a):
        print("One argument")
    def m1(self,a,b):
        print("Two arguments")
m=M_overloading()
# m.m1() #will get type Error ,py accepts last method only
m.m1(10,20)


# we can handle overloaded method requirements in python
class H_overloading:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("sum of 3 numbers:",a+b+c)
        elif a!=None and b!=None:
            print("Sum of 2 numbers:",a+b)
        else:
            print("Please give 2 or 3 args")
h=H_overloading()
h.sum(10,20)
h.sum(10,20,30)
h.sum(10)


# with variable no.of arguments
class Variables:
    def sum(self,*a):
        total=0
        for x in a:
            total=total+x
        print("Sum of numbers:",total)
v=Variables()
v.sum(10)
v.sum(10,230)
v.sum(10,20,30)


# Consrtuctor Overloading
class Test:
    def __init__(self):
        print("No argument")
    def __init__(self,a):
        print("One argument")
    def __init__(self,a,b):
        print("Two arguments")
# t=Test()    #typeError bcz it ecxcutes last constructor,args should be passed
# t1=Test(1)
t2=Test(1,2)

# constructer with default args
class D_arg:
    def __init__(self,a=None,b=None,c=None):
        print("Constructer with 0|1|2|3 no.of args")
d=D_arg()
d=D_arg(10,20)
d=D_arg(10,20,30)


# constructer with variable no.of arguments args
class Test:
    def __init__(self,*a):
        total=0
        for x in a:
            total=total+x
        print("sum of numbers:",total)
t=Test(10,2)
t=Test(10,293,3)

# Method Overriding
class Parent:
    def property(self):
        print("Gold+Money+Land")
    def marry(self):
        print("appalama")
class Child(Parent):
    def marry(self):
        super().marry()
        print ("Thamanna")
c=Child()
c.property()
c.marry()


# program for constructor overriding
class Parent:
    def __init__(self):
        print("Parent Constructer")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructer")
c=Child()

# pickling and unpickling
import pickle
class Employee:
    def __init__(self,eno,ename,eaddr):
        self.eno=eno
        self.ename=ename
        self.eaddr=eaddr
    def display(self):
        print(self.eno,'\t',self.ename,'\t',self.eaddr)
with open ('emp.dat','wb') as f:
    e= Employee(101,'sunny',"mumbai")
    pickle.dump(e,f)
    print("Pickling of employee obj completed...")
with open('emp.dat','rb') as f:
    obj=pickle.load(f)
    print("printing employee details for unpickling...")
    obj.display()
    
        
# pick.py 
import pickle
f=open('emp.dat','wb')
n=int(input('Enter the Employees:'))
for i in range (n):
    eno=int(input('Enter the number:'))
    ename=input('Enter the name:')
    eaddr=input('Enter the address:')
    pickle.dump(f)
print("Employee object pickled successfully...")

# eg
from abc import *
class Printer(ABC):
    @abstractmethod
    def printit(self,text):pass
    @abstractmethod
    def disconnect(self):pass
class EPSON(Printer):
    def printit(self,text):
        print("Printing from Epson")
        print(text)
    def disconnect(self):
        print("Printig completed on EPSON")
class HP(Printer):
    def printit(self,text):
        print("Printing from HP")
        print(text)
    def disconnect(self):
        print("Printing completed on HP")
pname=input("Enter the Printer name:")
classname=globals()[pname]
c=classname()
c.printit("Printing is Disconnected..")
c.disconnect()