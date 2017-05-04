a=int (raw_input("upper limit : "))
b=int(raw_input("lower limit : "))

for n in range(b,a+1):
    s=0
    temp=n
    a=len(str(n))
    while temp>0:
            d=temp%10
            s=s+d**a
            temp=temp/10


    if s==n:
          print n
        
