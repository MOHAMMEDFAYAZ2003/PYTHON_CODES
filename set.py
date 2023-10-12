# SET DATA TYPE 
s=set()
print(type(s))

# functions of the set
s={10,20}
s.add(30)
print(s)

s={'data',10,20}
s.update(range(5)) #args are not individual elements and these are iterable elements like list,
print(s)

#remove
s={1,2,3,4}
s.remove(4)
# s.remove(5) #it gives keyError,if element is not present
print(s)

# union 
x={1,2,2,3,4,5}
y={6,7,8,9}
print(x.union(y))
print(x|y)

# intersection
x={10,20,30,40}
y={10,30}
print(x.intersection(y))
print(x&y)

# difference
x={10,20,30}
y={10,30,40}
print(x-y)
print(y-x)

# symmetric difference
# removes the common elements
a={10,20,30,40}
b={10,30,40}
print(x^y)

s={i*i for i in range (10)}
print(sorted(s))

#To remove duplicate items
# s={1,2,3,'rat','cat',1,2}
s=eval(input())
s1=[]
for i in s:
    if i not in s1:
        s1.append(i)
print(s1)


# to find vowels in the string
w=input("Enter any word:")
s=set(w)
# l=['a','e','i','o','u']
# res=[]
# for i in w:
#     if i in l:
#         if i not in res:
#             res.append(i)
# print(res)

vowels={'a','e','i','o','u'}
print(s&vowels)


# pop : removes the random element in the set.
s={1,2,3,4,5,6,7}
s.pop()
print(s)

set1={10,9,True,90,"fayaz",49,69}
set2=set()
print(type(set1))
print(type(set2))
set1.remove(10)
set1.add(12)
print(set1)

a={'ram','nandhu','fayaz'}
b={'vijay','sai','fayaz'}
c=a.union(b)
d=a | b
print(d)
a.update(b)
print(a)

set3={1,2,3,4,5,6}
set4={5,6,7,8,9,0}
print(set4.issubset(set3))
print(set3 | set4)
print(set3 & set4)
print(set3.isdisjoint(set4))

a=int(input("Enter the Number : "))
for i in range(1,11):
    print(f"{a} x {i} = {a*i}")


