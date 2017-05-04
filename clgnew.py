#program to find quadratic equation
from math import sqrt
"""a=int(raw_input("Enter the coeff of a : "))
b=int(raw_input("Enter the coeff of b : "))
c=int(raw_input("Enter the coeff of c : "))
d=b**2-4*a*c
if d<0:
    print " The roots are imaginary "
elif d==0:
    print "roots are equal"
    x=-b/(2*a)
    print "This has only one equation : ",x
else :
    x1 = -b+sqrt(d)/(2*a)
    x2 = -b-sqrt(d)/(2*a)
    print "This equations two roots %s and %s "%(x1,x2)"""


#program to find the sum of numbers between two numbers
"""l_bound=int(raw_input("Enter the lower bound number : "))
u_bound=int(raw_input("Enter the upper bound number : "))
sum=0
for i in range (l_bound,u_bound+1):
    print "%s+"%i,
    sum=sum+i
print "\a is equal to ",sum
print "\nThe sum of numbers between %s and %s is %s"%(l_bound,u_bound,sum)"""



#program to print the multiplication table of the given number
"""num=int(raw_input("Enter the number : "))
ran1=int(raw_input("Mutiplication of %s from  "%num))
ran2=int(raw_input("                   to  : "))

print " MULTIPLICATION TABLE OF %s "%num
print " *************************"
for i in range(ran1,ran2+1):
    print" " ,i," * " ,num," = ",i*num"""

#program to print the factors of a number
"""n=int(raw_input("Enter the number : "))
print "The factors of %s are "%n,
for i in range(1,n+1):
    if n%i==0:
        print i,",","""


#program to check the number is perfect or not(perfect means sum of factors equal to the number itself
"""n=int(raw_input("Enter the number : "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i

if n==sum:
    print "it is a perfect number"
else:
    print "It is not a perfect number" """

#program to find all the perfect numbers        
"""for n in range(1,1000000):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i

    if n==sum:
        print n"""


#program to find sum of all even and odd numbers

"""lim=int(raw_input("Enter the limit : "))
s_even=0
s_odd=0
for i in range(1,lim+1):
        if i%2==0:
                s_even = s_even+i
        else:
                s_odd = s_odd+i

print "sum of odd numbers is %s \nsum of even numbers is %s"%(s_odd,s_even)"""


#program to find prime numbers in a range

"""lim=int(raw_input("Enter the limit : "))
f=0
for i in range (1,lim+1):
        for j in (2,i):
            if (i%j == 0):
                break
        else:
                print i"""


        
#program to make a pattern
"""c=1
for i in range(5):
        for j  in range(i):
                print c, 
                c=c+1
        print "\n" """


#program to make a pattern
"""c=1
for i in range(5):
        for j in range(i):
                print c,

        print "\n"
        c=c+1"""


#program to make a pattern
"""c=1
for i in range(4):
        for j in range(i):
                print j,
        print"\n" """


#program to find armstrong number in a range
"""def arm(a):
        su=0
        temp=a
        while temp>0:
                digit=temp%10
                su=su+digit**b
                temp=temp/10
        if (a==su):
                print a
a=int(raw_input("Enter the limit : "))
b=len(str(a))
for i in range(1,a+1):
        arm(i)"""

#program to find the distance formula

"""def dist(x1,x2,y1,y2):
        x=(x1-x2)**2
        y=(y1-y2)**2
        return "_/(%s-%s)**2+(%s-%s)**2 is %s"%(x1,x2,y1,y2,sqrt(x+y))

x1=int(raw_input("Enter x1 : "))
x2=int(raw_input("Enter x2 : "))
y1=int(raw_input("Enter y1 : "))
y2=int(raw_input("Enter y2 : "))
print dist(x1,x2,y1,y2)"""

#program to compute sum of series
"""def fact(n):
        f=1
        for i in range(1,n+1):
                f=f*i
        return f

x=int(raw_input("Enter value of x : "))
n=int(raw_input("Enter value of n : "))

su=0
for i in range(1,n+1):
        su=su+(x**i)/(fact(i))
print su       """



# program to remove the digits in a string
"""stri=raw_input("Enter the string  : ")
digits='1234567890'
new=""
for i in stri:
        if i not in digits:
                new=new+i                             
print new"""




#program to remove the punctuation in a string
"""stri=raw_input("Enter the string  : ")
pun="!@#$%^&*(){}[],.<>/?:;'_-\|"
new=""
for i in stri:
        if i not in pun:
                new=new+i                             
print new"""
        


#program to insert limited number of element in a list
"""lis=[]
lim=int(raw_input("Enter the number of elements to be added : "))
for i in range(lim):
        st=raw_input("Enter the element : ")
        lis.append(st)
print lis
lis[1]="will"
print lis"""


#program to sort the names in alphabetical order

"""lis=[]
lim=int(raw_input("Enter the limit : "))

for i in range(lim):
        a=raw_input("Enter name : ")
        lis.append(a)
lis.sort()
print lis"""

#program to split the number list to odd and even list
"""lis=[]
odd=[]
even=[]
lim=int(raw_input("Enter the limit : "))
for i in range(lim):
        a=int(raw_input("Enter the number : "))
        lis.append(a)
for j in lis:
        if j%2==0:
                even.append(j)
        else:
                odd.append(j)
print "The even list is ",even
print "The odd list is ",odd"""



#program to remove the duplicates from a list

"""lis=[]
no_dup=[]
lim=int(raw_input("Enter the limit : "))
for i in range(lim):
        a=raw_input("Enter the elements : ")
        lis.append(a)

for j in lis:
        if j not in no_dup:
                no_dup.append(j)
print no_dup"""


#program to abbreviate each word of a string
"""st=raw_input("Enter the string : ")
rev=""
rev=rev+st[0]
i=0
n=len(st)
while i<n:
        if st[i]==" ":
                rev=rev+st[i+1]
        i=i+1
u=rev.upper()
print u"""


#program to create dictionary and enter the name and age
"""dic={}
n=int(raw_input("Enter the limit : "))
for i in range (n):
        name=raw_input("Enter the name : ")
        age=int(raw_input("Enter the age : "))
        dic[name]=age
print dic"""


#program to create a dictionary of anme and age ,sort dictionary based on key value
"""dic={}
lim=int(raw_input("Enter the limit : "))
for i in range(lim):
        name=raw_input("Enter the name : ")
        age=int(raw_input("Enter the age : "))
        dic[name]=age

lis=dic.keys()
lis.sort()
for j in lis:
        print j,":",dic[j]"""




#program to find the number of letters and digits in a string
"""st=raw_input("Enter the string : ")
di=0
no=0
le=len(st)
for i in st:
        if i in "abcdefghijklmnopqrstuvwxyz":
                di=di+1
        elif i in "1234567890":
                no=no+1
print "The number of alphabets are : ",di
print "The number of digits are :",no"""



#program to create a file and write to file and remove all the punctuation marks on the text
"""st=raw_input("Enter the string : ")
f=open("new","w")
f.write(st)
f.close

f=open("new","r")
s=f.read()
pun="!@#$%^&*()_+-=:{}[];'<>?,./\|"
no_pun=""
for i in s:
        if i not in pun:
                no_pun=no_pun+i
print no_pun"""
       


#program to read a file and check if its odd or even and put it to separate files
"""f=open("new","w")
f.write("1 2 3 4 5 6 7 8 ")
f.close

ev=open("even","w")
od=open("odd","w")

f=open("new","r")
s=f.read()
lis=s.split()

for i in lis:
    if int(i)%2 ==0:
        ev.write(i)
    else:
        od.write(i)

ev=open("even","r")
od=open("odd","r")
print ev.read()
print od.read()"""


#program to convert decimal to binary
"""n=int(raw_input("Enter the decimal: "))
rev=""
while n>0:
    dig=n%2
    rev=str(dig)+rev
    n=n/2
print rev"""


#program to convert decimal to binary (my version)
"""n=int(raw_input("Enter the decimal : "))
while n>0:
    dig=n%2
    print dig,
    n=n/2
print dig"""



#program to convert binary to decimal
"""n=int(raw_input("Enter the decimal value : "))
x=0
dec=0
while n>0:
    dig=n%10
    dec=dec+dig*2**x
    x=x+1
    n=n/10
print dec"""


#program to check wheather given number is armstrong
"""n=int(raw_input("Enter the number : "))
le=len(str(n))
su=0
temp=n
while temp>0:
    dig=temp%10
    su=su+dig**le
    temp=temp/10
    
if su==n:
    print"It is a armsrong number"
else:
    print "It is not an armstrong number " """



#program to evaluate combination function using function

"""def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

n=int(raw_input("Enter the n value : "))
r=int(raw_input("Enter the r value : "))
print fact(n)/(fact(r)*fact(n-r))"""


#print all elements of a list as mattrix
"""lis=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
    for j in range(3):
        print lis[i][j],

    print"\n" """


#progam to find sum of two matrix
"""su=0
lis1=[[1,1,1],[2,3,4],[3,3,3]]
lis2=[[5,6,1],[2,5,4],[5,5,5]]
for i in range(3):
    for j in range(3):
        su=lis1[i][j]+lis2[i][j]
        print su,
    print"\n" """


#program to find sum of diagonal elements of mattrix
"""su=0
lis=[[1,1,1],[2,3,4],[3,3,3]]
for i in range(3):
    for j in range(3):
        if i==j:
            su=su+lis[i][j]
print su"""

#program to check if matrix is unit matrix
"""f=0
lis=[[1,2,1],[1,1,1],[1,1,1]]
for i in range(3):
    for j in range(3):
        if lis[i][j]==1:
            f=0
        else:
            f=1
            break
    if f==1:
        break

if f==1:
    print"It is not unit matrix"
else:
    print"It is a unit matrix" """


#program to find the transpose matrix
"""lis1=[[0,0,0],[0,0,0],[0,0,0]]
lis=[[5,6,1],[2,5,4],[5,5,5]]
for i in range(3):
    for j in range(3):
        lis1[i][j]=lis[j][i]

for k in range(3):
    for l in range(3):
        print lis1[k][l],
    print"\n" """


#program to find given mattrix is symmetric
"""lis1=[[0,0,0],[0,0,0],[0,0,0]]
lis=[[1,1,1],[1,1,1],[1,1,1]]
for i in range(3):
    for j in range(3):
        lis1[i][j]=lis[j][i]
if lis==lis1:
    print"its is symmetric"
else:
    print"it is not symmetric" """


#program to find matrix multiplication
"""lis1=[[1,1,1],[2,3,4],[3,3,3]]
lis2=[[5,6,1],[2,5,4],[5,5,5]]
lis=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        lis[i][j]=lis1[i][j]*lis2[j][i]
for k in range(3):
    for l in range(3):
        print lis[k][l],
    print"\n" """

#program to ask for elements in a matrix
"""a=0
b=0
lis1=[[1,1,1],[2,3,4],[3,3,3]]
for i in range(3):
    for j in range(3):
       lis1[i][j]= raw_input ("row %s and coloumn %s : "%(i+1,j+1))
       
for k in range(3):
    print"|",
    for l in range(3):
        print lis1[k][l],
    print"|\n" """




#program to find factorial using recursion
"""def fact(n):
    if n<=1:
        return n
    else:
        return n*fact(n-1)
        
a=int(raw_input("Enter the number : "))
print fact(a)"""



#program to find fibbinocci series to  a limit
"""lim=int(raw_input("Enter the limit : "))
a=0
b=1
c=0
print a
print b
for i in range(lim-2):
    c=a+b
    print c
    a=b
    b=c"""


#program to find the fibanocci series using recursion
"""def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

lim=int(raw_input("Enter the limit : "))
for i in range(lim):
    print fib(i)"""























   


