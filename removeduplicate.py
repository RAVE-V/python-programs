lim=int(raw_input("Enter the size of list : "))
list=[]
i=0
newlist=[]
for i in range(0,lim):
    a=int(raw_input("Enter the number : "))
    list.append(a)
print "The main is ",list


for m in list:
    if m not in newlist:
        newlist.append(m)

print"The list where the duplicate is removed is ",newlist
q=tuple(list)
print q
