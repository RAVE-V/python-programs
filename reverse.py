lim=int(raw_input("Enter the limit : "))
d=0
rev=0
while (lim !=0):
       d=lim%10
       rev=rev*10+d
       lim=lim/10
print rev
