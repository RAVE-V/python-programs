list1=[[1,1,1],[2,2,2],[1,1,1]]
list2=[[1,1,1],[1,1,1],[1,1,1]]
#list3=[[0,0,0],[0,0,0],[0,0,0]]
for k in range(3):
        print '|',
        for l in range(3):
                print list1[k][l],
        print '|\n'
print'*********'
f=0
for i in range(3):
        for j in range(3):
                list2[i][j]=list1[j][i]
print 'The tranpose :'
for m in range(3):
        print '|',
        for n in range(3):
                print list2[m][n],
        print '|\n'
