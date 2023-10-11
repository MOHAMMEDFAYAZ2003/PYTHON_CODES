#LIST
l=eval(input())
print(type(l))
print(l)

# l1=list(range(10))
# print(l1)

#split function
s="python"
l=s.split()
print(l)

#Traversing : The sequential access of each element in the list is called Traversing.
n=[1,3,4,5,56,6,6,]
i=0
while i < len(n):
    print(n[i])
    i+=1

#for loop
n=[0,1,3,5,6]
for i in range(len(n)):
    print(i)

#Elements indexwise (+,-index)
l=['a','b','c']
x=len(l)
for i in range(x):
    print(l[i],"positive index",i)
    print(l[i],"negative index",i-x)

l=[1,2,3,4,5]
# l1=l.count(3)
# print(l1)
l.insert(1,22)
print(l)

order1=['chicken','Mutton','Biryaani']
order2=['chapathi','Roti','idly']
order1.extend(order2)
print(order1)

l1=[10,20,30,40,50]
l1.remove(20)
print(l1)

l2=[10,20,30,40,50]
n=int(input())
if n in l2:
    l2.remove(n)
    print("Removed Successfully")
else:
    print("Specified element is not available...")


#aliasing:-->The process of giving another reference variable to the existing list is called as aliasing.

x=[10,20,30,40,50]
y=x     #aliasing
y[0]=333
print('x:',x)
print('y:',y)

#-->The process of creating exactly duplicate independent object is called as cloning.
x=[10,20,30,40,50]
y=x.copy()#cloning
y[0]=333
print('x:',x)
print('Y:',y)

x=[10,20,30,40,50]
y=x[:] #cloning
y[1]=333

# a=[1,2,3]
# b=[4,5,6]
# c=a+b
# d=a*2
# print(c)
# print(d)

#Nested List:
n=[10,20,[30,40]]
print(n[0])
print(n[2])
print(n[2][1])

# Nested list as matrix:
n=[[10,20,30],[40,50,60],[70,80,90]]
print(n)
print('Elements by row wise:')
for r in n:
    print(r)
print("Elements by Matrix style:")
for i in range (len(n)):
    for j in range (len(n[i])):
        print(n[i][j],end=' ')
    print()

#list comprehension
#Print first 10-numbers squares in list format.
l=[]
for i in range(0,11):
    l.append(i * i) #noraml progarm
print(l)

l=[i*i for i in range(0,11)]
print(l) #list comprehension

#Print only even numbers
l=[i for i in range(1,11) if i%2==0]
print(l)


# word = 'the quick brown fox jumps over the lazy dog'
# o/p:[['THE',3],['QUICK',5],['BROWN',5],['FOX',3]........['DOG',3]]
sentence=input()
sentence1=sentence.split()
l=[[w.upper(),len(w)] for w in sentence1]
print(l)


#to display unique vowels present in the given string
word=input("Enter a string:")
vowels=['a','e','i','o','u']
found=[]
for i in word:
    if i in vowels:
        if i not in found:
            # print(i,end=" ")
            found.append(i)
print("The vowels in word:",found)

##TUPLE
t=()
print(type(t))

t1=(10,)
print(type(t1))

t1=(10,20)
t2=(30,40)
print(t1+t2) #cancatination

#sort
t=(40,50,30,40,60,78)
t2=sorted(t)
print(t2)  #it returns in the form of list
print(min(t2))
print(max(t2))

# tuple packing and unpacking
# we can create a tuple by using package of variables
a=1
b=2
c=3
d=4
t=a,b,c,d  #packing
print(t)

t1=[1,2,3,4,5]
a,b,c,d,e=t1      #unpacking
print(t1)

# #tuple comprehension
x=(i**2 for i in range(10))
print(type(x))   #<class 'generator'>
print(x) #<generator object <genexpr> at 0x000001DAF6474350> #it is a memory location
for i in x:
    print(i,end=" ")
#"""TUPLE IS NOT SUPPORT COMPREHENSIONS"""