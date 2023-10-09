# Decorator is a function which can take a function as a argument and extend its functionality and returns modified function with extended functionality.
#
# 	Input function---->Decorator Function----->o/p func with extended fun.....
#
# The main objective of decorator function is we can extend the functionality of existing functions without modifies that function.
def greet(a):
    def b():
        print("Good Morning")
        a()
        print("Thanks for using our application")
    return b
@greet
def m1():
    print("Hello World")

def m2(a,b):
    print(a+b)

m1()

# To know current working directory
import os
cwd=os.getcwd()
print("Current working directeries:",cwd)


# To create a sub directory in the current working  directory.
import os
a=os.mkdir('f_p')
print('My sub working Directery:',a)

# To create sub directory in my sub directory (f_p)
import os
os.mkdir('f_p/new f_p')
print("My sub2 directory created inside f_p")

# To create multiple directories like sub1 in that sub2 in that sub3
import os
os.makedirs('sub1/sub2/sub3')
print("sub1 sub2 sub3 dirs created")

# To remove a directory
import os
os.rmdir('sub1/sub2/sub3')
print("sub3 is deleted.....")

# To remove multiple directories in the path
import os
os.removedirs('sub1/sub2/sub3')
print('All directeries all removed.....')

# To rename a directory
import os
os.rename('p_f','f_p')
print('f_p dir is renamed as p_f')

# To know content of directory
import os
print(os.listdir('.'))
# If we want the content of a directory including sub directories then we should go for walk() function


# To display all contents of current directory including sub directories
import os
for dirpath,dirnames,filenames in os.walk('.'):
    print('Current dir path:',dirpath)
    print('Directeries:',dirnames)
    print('Files:',filenames)
    print()

# How to get information about file
# -->We can get statistics of a file like size, last accessed time, last modified time etc...by using stat() function.

import os
stats=os.stat('12345.txt')
print(stats)

import os
from datetime import *
stats=os.stat('12345.txt')
print('file size:',stats.st_size)
print('File last accessed time:',datetime.fromtimestamp(stats.st_atime))
print('File last modified time:',datetime.fromtimestamp(stats.st_mtime))