#swaping of two numbers
a=int(input("Enter the value A:"))
b=int(input("Enter the value B:"))
a,b=b,a
print("After swaping")
print("A=",a)
print("B=",b)


#write a program to return given word is a palindrome or not
a=int(input("Enter the Number : "))
b=str(a)
rev_b=b[::-1]
print("Reversed Number is ",rev_b)
if rev_b==b :
    print("It is a Palindrome")
else:
    print("It is not a Palindrone")

#To print all Non-Empty substring
str=input("Enter the string : ")
for i in range(len(str)):
    for j in range(i+1,len(str)+1):
        print (str[i:j],end=" ")
    print()

## To get all substrings in a List
str=input("Enter the string : ")
list1=[]
for i in range (len(str)):
    for j in range (i+1,len(str)+1):
        list1.append(str[i:j])
print(list1)

##Check wheater substring is present in string
a=input("Enter the String : ")
b=input("Enter the substring : ")
if b in a :
    print(b,"is present in ",a)
else:
    print(b,"is not presnt in ",a)

# write a program to give everyday temperature
daily_temp={'sun':10,'mon':20,'tues':30,'wed':40,'thurs':50,'fri':60,'sat':70}
dayname={'sun':'Sunday','mon':'Monday','tues':'Tuesday','wed':'Wednesday',
         'thurs':'Thursday','fri':'Friday','sat':'Saturday'}
day=input("Enter'sun','mon','tues','wed','thurs','fri','sat':")
print("The Temperature on",dayname[day],"was",daily_temp[day])