s="sunny"
for i in s :
    print(i)


s="suresh"
i=0
for x in s :
    print("The charecters in S are :",i,x)
    i=i+1


#To print tables
n=int(input("Enter Number :"))
for i in range (1,21):
    m=n*i
    print(n,"X",i,"=",m)


# a=[0,1,2,3]
# for a[-1] in a :
#     print(a[-1])


#To print the character with the index number
a=input("Enter any String : ")
i=0
for x in a:
    print("The Character present at ",i,"index is",x)
    i+=1


# for i in range(10):
#     print("Hi")

# for i in range (1,21,2):
#     print(i)

# for i in range (21):
#     if i%2!=0:
#         print(i)

#To display numbers from 10-0
for i in range(10,0,-1):
    print(i)

#To print table
a=int(input("Enter the table number : "))
for i in range(1,11):
    result=a*i
    print(a,'x',i,'=',result)
    #list1=['apple','banana','tomato']
#list1=[['apple',1],['mango',2],['tomato',3],['banana',4]]

#for item in list1:
#    print(item)
#for item,lollypop in list1:
#    print(item,' have',lollypop)

items=['int','float','banana',2,4,5,6,44,55,66,77,88]
for item in items:
   if str(item).isnumeric() and item>6:
       print(item)

##while loop
#i=0
#while(i<45):
#   print(i)
 #   i=i+1


items=['a','f','t',1,2,3,4,55,66,77,88]
for item in items:
   if str(item).isnumeric() and item>6:
       print(item)