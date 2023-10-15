# 3-types of methods

# 1.instance method
# 2.class method
# 3.static method

# 1.instance method

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(f"Hi {self.name} ")
        print(f"Your marks are :{self.marks}")
    def grade(self):
        if marks>=60:
            print("You got 1st Grade")
        elif marks>=50:
            print("You got 2nd Grade")
        elif marks<=35:
            print("Congrats you are Failed....")
        else:
            print ("Plz...Give valid input")

# name=input('Enter your name:')                #for single student
# marks=int(input("Enter your marks:"))
# s=Student(name,marks)
# s.display()
# s.grade()
n=int(input("Enter the no.of students:"))       #for multiple students
for n in range(n):
    name =input('Enter your name:')
    marks=int(input("Enter your marks:"))
    s=Student(name,marks)
    s.display()
    s.grade()
    print()

2.class method

class Rabbit:
    legs=4
    @classmethod
    def walk(cls,name):
        print("{} walks with {} legs".format(name,cls.legs))
# Rabbit.walk('Dog')
# Rabbit.walk('Cat')
r=Rabbit()
r.walk('fag')

# to check no.of objects created for class
class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def no_of_objects(cls):
        print("no.of objects created for Test Class:",cls.count)
t1=Test()
t2=Test()
t3=Test()
t4=Test()
t2.no_of_objects()

# 3.static method
class Fayaz:
    @staticmethod
    def add(x,y):
        print ("x+y = ",x+y)
    def mul(x,y):
        print("x*y = ",x*y)
Fayaz.add(2,3)
Fayaz.mul(3,4)



# passing members of one class to another class
# We can access the members of one class inside another class

class Employee:
    def __init__(self,ename,esalary,eph):
        self.ename=ename
        self.esalary=esalary
        self.eph=eph
    def display(self):
        print("Employee name :",self.ename)
        print("Employee salary:",self.esalary)
        print("Employee number:",self.eph)
class Test:
    def modify (emp):
        emp.esalary+=8000
        emp.display()
e=Employee("Indra",20000,9390037986)
Test.modify(e)


# # Inner classes
# Eg-1
class Outer :
    def __init__(self):
        print("Outer class")
    class Inner():
        def __init__(self):
            print("Inner Class")
        def m1(self):
            print("Inner class method")
# o=Outer()
# i=o.Inner()
# i.m1()
i=Outer().Inner().m1()
Outer().Inner().m1()


# Eg-2
class Human:
    def __init__(self):
        self.name='Ramesh'
        self.Head=self.Head()
        self.brain=self.Head.Brain()
    def display(self):
        print('Hello',self.name)
    class Head:
        def talk(self):
            print('Taking....')
        class Brain:
            def think(self):
                print("Thinking???")
h = Human()
h.display()


#nested methods
# A method inside the method is called nested method
class Test:
    def m1(self):
        def calc(a,b):
            print('Sum:',a+b)
            print('Product:',a*b)
            print('Division:',a//b)
            print('Difference:',a-b)
            print ()
        calc(6,3)
        calc(5,7)
t=Test()
t.m1()
