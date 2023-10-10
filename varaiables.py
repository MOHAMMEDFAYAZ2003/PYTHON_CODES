# Q.Where we can declare instance variables?
# 1.Inside constructor:
class Employee:
    def __init__(self):
        self.eno = 101
        self.ename = 'rahul'
e = Employee()
print(e.__dict__)

# 2.Inside instance method:
# We can aslo declare instance variables inside method by using self variable.
class Test:
        def __init__(self):
            self.a=10
            self.b=20
        def m1(self):
            self.c=30
t = Test()
t.m1()
print(t.__dict__)


# 3.Outside of the class:
# We can also add instance variables outside of a class to a particular object.
class Fayaz:
    def __init__(self):
        self.a=1
        self.b=2
    def m1(self):
        self.c=3
f=Fayaz()
f.m1()
f.d=4
print(f.__dict__)

#How to access instance variables:
#We can access instance variables with in the class by using self and outside of the class by using object reference.
class Shiva:
    def __init__(self):
        self.a=1
        self.b=2
    def m1(self):
        self.c=3
s=Shiva()
s.m1()
print(s.a,s.b,s.c )

#How to delete instance variables from the object:
# 1.Within the class:
# 	del self.variablename
class Indra:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
    def method(self):
        del self.c
i =Indra()
i.method()
print(i.__dict__)

# 2.Outside of the class:
# 	del objectreference.variablename
class Fayaz:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
    def m1(self):
        self.d=40
f1=Fayaz()
f2=Fayaz()
del f1.c
print(f1.__dict__)
print(f2.__dict__)

# Eg:
class Test:
    def __init__(self):
        self.a=10
        self.b=20
t1=Test()
t1.a=111
t1.b=222
t2=Test()
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)

#Eg:
class Test():
    x=10
    def __init__(self):
        self.y=20
t1=Test()
t2=Test()
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
Test.x=22
t1.y=33
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)

# Various places to declare static variables:
class Nandu:
    a=10
    def __init__(self):
        Nandu.b=20
    def m1(self):
        Nandu.c=30
    @classmethod
    def m2(cls):
        Nandu.d1=40
        Nandu.d2=50
    @staticmethod
    def m3():
        Nandu.e=60
t=Nandu()
t.m1()
t.m2()
t.m3()
Nandu.f=70
print(Nandu.__dict__)

# How to access static variables:
class Fayaz:
    a=10
    def __init__(self):
        print(Fayaz.a)
        print(self.a)
    def m1(self):
        print(self.a)
        print(Fayaz.a)
    @classmethod
    def m2(cls):
        print(cls.a)
        print(Fayaz.a)
    @staticmethod
    def m3():
        print(Fayaz.a)
print(Fayaz.a)
f=Fayaz()
f.m1()
f.m2()
f.m3()

# Where we can modify the value of static variables:
class Bunny:
    a=10
    @classmethod
    def m1(cls):
        cls.a=22
    @staticmethod
    def m2():
        Bunny.a=33
print(Bunny.a)
Bunny.m1()
print(Bunny.a)
Bunny.m2()
print(Bunny.a)

''' If we change the value of static variable by using either self or object reference
variable, then the value of static variable wont be changed, just a new instance variable
with that name will be added to that particular object.'''

#Eg:
class Test:
    a=100
    def m1(self):
        self.a=333
t=Test()
t.m1()
print(Test.a)
print (t.a)

#Eg:
class Sunny:
    a=10
    def __init__(self):
        self.b=20
t1=Sunny()
t2=Sunny()
Sunny.a=333
t1.b=444
print('t1:',t1.a,t2.b)
print('t2:',t2.a,t2.b)

#Eg:
class Test:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        self.a=333
        self.b=999
t1=Test()
t2=Test()
t1.m1()
print('t1:',t1.a,t2.b)
print('t2:',t2.a,t2.b)
print(Test.__dict__)
print(t1.__dict__)

# How to delete static variables of a class:
class Test:
    a=10
    @classmethod
    def m1(cls):
        del cls.a
Test.m1()
print(Test.__dict__)

#Local variables
class local:
    a=10
    def m1(self):
        a=100
        print(a)
    def m2(self):
        b=200
        print(b)
l=local()
l.m1()
print(local.a)
print(b)    #name error

## program for student marks
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(f"Hi {self.name}")
        print(f"Your marks are {self.marks}")
    def grade(self):
        if self.marks>=60:
            print("You got First Grade")
        elif self.marks>=50:
            print("You got second Grade...")
        elif self.marks>=35:
            print("You got Third Grade...")
        elif self.marks<=35:
            print("Congratulations U are Failed...")
        else:
            print("Please Enter the valid input...")
s=Student("fayaz",12)
n=int(input("Enter no.of students:"))
for i in range(n):
    name=input("Enter your name:")
    marks=int(input("Enter your Marks:"))
    s=Student(name,marks)
    s.display()
    s.grade()
    print()

#classmethod
# Eg:
class Rabbit:
    legs=4
    @classmethod
    def walk(cls,name):
        print("{} walks with {} legs".format(name,cls.legs))
# Rabbit.walk('Dog')
# Rabbit.walk('Cat')
r=Rabbit()
r.walk('fag')
