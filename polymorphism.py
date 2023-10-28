#Duck typing philosophy of python
class Duck:
    def talk(self):
        print("Quack..")
class Dog:
    def talk(self):
        print("Bow..")
class Cat:
    def talk(self):
        print("Meow..")
class Goat:
    def talk(self):
        print("Myaah..")

# def f1(obj):
#     obj.talk()
    
# l=[Duck(),Dog(),Cat(),Goat()]

# for obj in l:
#     f1(obj)
def display(Goat):
    Goat.talk()

g=Goat()
g.talk()


# hasattr() function
class Duck:
    def talk (self):
        print("Quack..")
class Dog:
    def bark(self):
        print("Bow")
def display(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()
l=[Dog(),Duck()]
for obj in l:
    display(obj)
    
# class Animal:
#     name="Lion"
#     age=20
# a=Animal()
# print(hasattr(a,'name'))
# print(hasattr(a,'age'))
# print(hasattr(a,'lenght'))

# hasattr() function
class Duck:
    def talk (self):
        print("Quack..")
class Dog:
    def bark(self):
        print("Bow")
def display(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()
l=[Dog(),Duck()]
for obj in l:
    display(obj)


    
#Overloading
#Operator Loading
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
b1=Book(10)
b2=Book(20)
# print(b1+b2)    #will get Error:"have to use Magic Method __add__"
print(b1.pages+b2.pages)
print(b1+b2)


# HOW TO ADD MULTIPLE OBJECTS
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        total=self.pages+other.pages
        return Book(total)
b1=Book(100)
b2=Book(200)
b3=Book(300)
b4=Book(400)
bx=b1+b2+b3+b4
print(bx.pages)

#program to overload multiplication operator to work on Employee objects
class Employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def __mul__(self,other):
        return self.sal*other.days
class Timesheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days
    def __mul__(self,other):
        return self.days*other.sal
e=Employee("sunny",1000)
t=Timesheet("sunny",30)
print("This month salary:",e*t)
print("This month salary:",t*e)


