def fact(a):
    f=1
    for i in range(1,a+1):
        f=f*i
    return f

n=int(raw_input('Enter n : '))
r=int(raw_input('Enter r : '))

print fact(n)/(fact(r)*fact(n-r))
