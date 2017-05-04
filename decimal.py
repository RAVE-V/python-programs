def binary():
    n=int(raw_input("Enter decimal : "))
    bi=""
    while n>0:
        d=n%2
        print d,
        n=n/2

def deci():
    n=int(raw_input('Enter binary : '))
    x=0
    dec=0
    while n>0:
        d=n%10
        dec=dec+d*2**x
        x=x+1
        n=n/10
    print dec

print("Convert to decimal or to binary ?")
ans=raw_input('b for binary and d for decimal :  ')
ans.lower()
if ans=='b':
    binary()
elif ans=='d':
    deci()



    
