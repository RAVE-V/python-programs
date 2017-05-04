from __future__ import print_function

import datetime,os,calendar
from math import pi
from datetime import date


now =datetime.datetime.now()
print ("the current time is : ",now)
print (now.strftime("%d-%m-%y  %h:%m"))


"""r=int(raw_input("Enter the radius : "))
area= r*r*pi
print area
raw_input("Enter to cntue")
#os.system('pause')"""

#program to list senternce separted by comma
"""n=raw_input("Enter the things separated by comma : ")
list =n.split(",")
print list
tup = tuple(list)
print tup """

#program to find the extension of a file
"""filename=raw_input("Enter the filename : ")
f_ext=filename.split(".")
print "The extension of the file is ",repr(f_ext[-1])#The extension of the file is  'java'
print "The extension of the file is ",f_ext[-1]  #The extension of the file is  java"""


#program to print the first and last elements of the list
""""inp=raw_input("Enter the things to be in the list separetd by comma : ")
lis=inp.split(",")
print "the first and the last elements are %s and %s"%(lis[0],lis[-1])"""

#program to print n+nn+nnn from the input
"""n=int(raw_input("Enter the value : "))
d=n+n*n+n*n*n
print "the solution of %s+%s*%s+%s*%s*%s is %s"%(n,n,n,n,n,n,d)"""


#program to execute retrive element s from a list
"""tup=(11,12,2016)
print "The exams will start on %s-%s-%s"%(tup)"""


#program to print the docstring of a function
"""fun=raw_input("Enter the fuction syntax ")
print fun.__syntax__  """




#program to print the calender of a month using the calender module
"""y=int(raw_input("Enter the year : "))
m=int(raw_input("Enter the month : "))
print calendar.month(y,m)"""


#program to find the difference between two dates in days(does'nt work)
"""fdate=date(2016,7,2)
ldate=date(2106,7,11)
diff=ldate-fdate
print diff.days"""


#progam to print volume of sphere
"""r=int(raw_input("Enter the radius : "))

v=4.0/3.0*pi*r**3
print"The volume of the sphere of radius %f is %f"%(r,v)"""



#program to print reverse the string(using for loop)
"""st=raw_input("Enter the string :")
rev=""
for i in st :
    rev=i+rev
print rev"""  
    


#program to get difference between a given number and 17,if the number is greater than 17 return double the absolute value
"""nu=int(raw_input("Enter the number : "))
if nu<=17:
    print "The difference is",17-nu
else:
    a=2*(abs(17-nu))
    print"The double of absloute difference is ",a"""



#program to check if palindrome without reversing the string
"""st=raw_input("Enter the string : ")

a=st[::-1]
print a
if st==a:
    print "it is a palindrome"
else:
    print"Its not a palindrome" """





#program to test whether a number is within 100 of 1000 or 2000

"""def th(n):
    return ((abs(1000-n)<=100)) or ((abs(2000-n)<=100))
a=int(raw_input("Enter the number : "))
print th(a)"""



#program to calculate sum of three given numbers and if all the numbers are equal then take the thrice
"""a=int(raw_input("Enter the number : "))
b=int(raw_input("Enter the number : "))
c=int(raw_input("Enter the number : "))
def sum(a,b,c):
    su=a+b+c
    if a==b==c:
        su=su*3
    return su
print (sum(a,b,c))"""




#program to get new string with 'ls' if ls is not present in the string
"""def ls(st):
    if len(st)>=2 and st[:2]=="ls":
        return st
    return "ls"+st
st=raw_input("Enter the string : ")
print ls(st)"""




#program to print n copies of the given string
"""def cop(st,n):
    result=""
    for i in range(n):
        result=result+st
    return result


st=raw_input("Enter the string : ")
n=int(raw_input("Enter the number of copies that needed to be printed : "))
print(cop(st,n)) """


#program to print n copies of the first two character of the given string and i f the string has less than two character then return n copies of the given string
""""def cop(st,n):
   
    if len(st)>2:
        cut=st[:2]
        a=cut*3
        return a
    else:
        return st*n
st=raw_input("Enter the string : ")
n=int(raw_input("Enter the copies number : "))
print cop(st,n)"""



#progam to form a word from all the vowels in the given string
"""def vow(st):
    re=""
    for i in st:
        if i in "aeiouAEIUO":
            re=re+i
    return re
st=raw_input("Enter the  string : ")
print vow(st)"""


#program to find if the given value is present in the given set of values
"""lis=[1,2,3,5,7]
n=int(raw_input("Enter the value : "))
if n in lis:
    print "yes its included "
else:
    print "no its's not included" """





#program to print histogram of given list of numbers
"""def hist(item):
    for n in item:
        output=''
        times=n
        
        while times>0:
            
            output+='*'
            times=times-1
        print output
hist([2,3,4,5])"""




#program to check whether a file is present
"""import os.path
open('new','w')
print os.path.isfile('new')"""



#program to find if python shell is 64 bit or 32 bit
"""import struct
print (struct.calcsize('P')*8)"""


#program to get os name,platform and release inforamtion
"""import platform,os
print os.name
print platform.system()
print platform.release()"""




#program to locate local python site package
"""import site
print site.getsitepackages()"""



#program to call external commands in python(not working)
"""from subprocess import call
call(["ls","-l"])"""



#program to find the path and name of the file currently used
"""import os
print ("current file name :" ,os.path.realpath(__file__))"""


#program to find the number of cpu
"""import multiprocessing
print multiprocessing.cpu_count()"""


#program to determine th profiling of python programs(all the processes behind python an dits time)
"""import cProfile
def sum():
    print 1+2
cProfile.run('sum()')"""



#program to print stderr

"""import sys

def eprint(*args,**kwargs):
    print(*args,file=sys.stderr,**kwargs)
eprint("abc","efg","xyz",sep="--")"""




#program to find environment variables
"""import os
print (os.environ)#environment variables
print ("\n")
print (os.environ['HOME'])
print ("\n")
print (os.environ['path'])"""



"""#program to get current username
import getpass
print (getpass.getuser())"""


#program to get the exection time of program
"""import time
def tim(n):
    start=time.time()
    print ("The acuurate start time is ",start)
    s=0
    for i in range (1+n+1):
        s=s+1
    end=time.time()
    print ("The accurate  enc time is",end )
    return end-start
n=int(raw_input("Enter the limit : "))
print ("Time taken for the process to complete is",tim(n))"""






#program to print the banner
"""import os
import time
WIDTH=79
message="hello!".upper()
printedmessage=["","","","","","",""]
character={" ":[" ",
                " ",
                " ",
                " "],
           "E":["*****",
                "*    ",
                "*    ",
                "***  ",
                "*    ",
                "*    ",
                "*****",],
           
           "H":["*   *",
                "*   *",
                "*****",
                "*   *",
                "*   *",],
           
           "O":["*****",
                "*   *",
                "*   *",
                "*   *",
                "*****"],
           
           "L":["*    ",
                "*    ",
                "*    ",
                "*    ",
                "*****"],
           "!":["  *  ",
                "  *  ",
                "  *  ",
                "  *  ",
                "     ",
                "  *  ",],
           }


for row in range(4):
    for char in message:
        printedmessage[row]+=(str(character[char][row])+"  ")
offset=WIDTH

while True:
    os.system("cls")
    print(" "*offset + printedmessage[row][max(0,offset*-1):WIDTH-offset])
    offset=-1
    if offset<=((len(message)+2)*6)*-1:
        offset=WIDTH
        time.sleep(0.05)"""
        









           



























