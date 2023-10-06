
def function(a):
   print(a+"Hello World")
function("apple ")
function("mango ")

def function(a,b):
   print(a+" "+b)
function("apple","banana")

a,b=1,3
c=a+b
def function1 (c):
   print("Ur function is ",c)
function (c)

def function2(a,b):
   average=(a+b)/2
   print(average)
  # return average
function2(5,6)
#v=function2(5,6)4
#print(v)

#Doc string
def function3(a,b):
    """This will not work for 3 numbers"""
    average=(a+b)/2
    print('The average is ',average)
    return average
print(function3.__doc__)


#check whether the given number is even or odd?
def even_odd(num):
    if num%2==0:
        print("Even Number")
    else:
        print("Odd Number")
even_odd(4)

#function to find factorial of given number
def fact(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
for i in range(1,6):
    print("The factorial of ",i,"is",fact(i))

# break_continue
i=0
while (i<45):
   print(i+1,end="")
   i+=1

i=0
while(True):
   print(i+1)
  if (i==45):
       break
   i=i+1


i=0
while(True):
    if (i+1<5):
        i=i+1
        continue
    print(i+1)
    if(i==44):
        break
    i=i+1