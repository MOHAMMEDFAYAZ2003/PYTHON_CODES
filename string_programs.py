#To reverse the internal content of each word
string=input("Enter any string:")
s=string.split()
r=[]
i=0
while i<len(s):
    r.append(s[i][::-1])
    i+=1
print(' '.join(r))


#to merge of 2 string into a single string by taking cahracters alternatively
s1=input()
s2=input()
output=""
i,j=0,0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output+=s1[i]
        i+=1
    if i<len(s2):
        output+=s2[j]
        j+=1
print(output)


#to sort the characters of string and first alphabate symbols followed by numreic values
s=input()
s1=s2=output=""
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in sorted(s1):
    output=output+x
for x in sorted(s2):
    output=output+x
print(output)

I/P:A1B2C3D4
O/P:ABCD1234


#WRITE A PROGRAM FOR FOLLOWING REQUIREMENT I/P:A4B3C2,O/P:AAAABBBCC
s=input()
output=""
for i in s:
    if i.isalpha():
        output=output+i
        previous=i
    else:
        output=output+previous*(int(i)-1)
print(output)


#To perform following activity i/p:a4k3b2
s=input("Enter the String:")
output=""
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        b=(ord(previous)+int(x))
        output+=chr(b)
print(output)


#to remove the duplicate charecters from the given string
str=input("Enter any String:")
l=[]
for i in str:
    if i not in l:
        l.append(i)
print(''.join(l))

#Alternative method
a=input("Enter any String:")
print(''.join(set(a)))
