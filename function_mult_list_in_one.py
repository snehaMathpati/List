a=[[3,2,4,6],[7,5,4,9]]
i=0
while i<len(a):
    j=0
    b=[]
    while j<len (a[i]):
        b.append(a[i][j])
        j=j+1
    i=i+1
print(b)
