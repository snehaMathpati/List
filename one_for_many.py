def dupl():
    a=["sita","sita","ram","laxm","sita","ram","laxm"]
    i=0
    dup=[]
    while i<len(a):
        if a[i] not in dup:
            dup.append(a[i])
            b=b.sort(dup)
        i=i+1
    print(b)
dupl()