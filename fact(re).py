def fact(b):
       if (b<=1):
              return b
       else:
              return b*fact(b-1)


a=int(raw_input("Enter number: "))
print fact(a)
