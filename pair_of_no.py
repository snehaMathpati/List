def num():
    number=30
    n=[10,11,12,13,14,17,18,19]
    x=[]
    i=0
    while i<len(n):
        y=[]
        j=0
        while j<len(n):
            if n[i]+n[j]==number and n[i]<n[j]:
                y.append(n[i])
                y.append(n[j])
                x.append(y)
            j=j+1
        i=i+1    
    print(x)
num()