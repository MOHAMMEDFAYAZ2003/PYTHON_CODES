d={}
print(type(d))

# to add elements in the dict
d={}
d['a']=100
d['b']=200
d['c']=300
print(d)

# how to access the data from the dict
d={1:'sunday',2:'monday',3:'Tuesday'}
print(d[1])
print(d[2])


# no.of students and their marks
res={}
n=int(input("Enter number of students:"))
i=1
while i <= n:
    name=input("Enter your name:")
    marks=int(input("Enter your Marks:"))
    res[name]=marks
    i=i+1
print("Name of the student",'\t',"% of Marks")
for x in res:
    print('\t\t',x,'\t\t',res[x])

# Functions of dict
# pop()
d={1:"bat",2:'rat',3:'mat'}
d=d.pop(1) #in dict we have to give atleast one argument 
print(d)

# popitem() 
d={1:"bat",2:'rat',3:'mat'}
d.popitem()
print(d)


# .keys()
d={1:"bat",2:'rat',3:'mat'}
d1=d.keys()
print(d1)

# # .values()
d={1:'one',2:'two',3:'three',4:'four'}
# e=d.values()
# print(e)
print(d.values())
for i in d.values():
    print(i)


# .items()
d={1:'one',2:'two',3:'three',4:'four'}
d1=d.items()
print(d1)
for i in d1:
    print(i)

# setdefault
d={100:'sunny',200:'bunny',300:'vinny'}
print(d.setdefault(100,'pinny'))
print(d)
print(d.setdefault(400,'pinny'))
print(d)

# update
d={100:'sunny',200:'bunny',300:'vinny'}
d1 = {'a':'apple','b':'banana'}
d.update(d1)
print(d)
d.update([(333,'A'),(999,'B')])
print(d)