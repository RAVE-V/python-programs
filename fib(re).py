def fib(a):
       if a<=1:
              return a
       else:
              return fib(a-1) +fib(a-2)
              
lim=int(raw_input("Enter the limit : "))
for i in range (lim):
       print fib(i)
