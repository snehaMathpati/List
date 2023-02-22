def add():
    
    sum=0
    t=0
    # avg=0
    i=1
    while i<=3:
        u1=int(input("enter the no:"))
        sum=sum+u1
        t=t+1
        avg=sum/t
        i=i+1
    print(avg)
    print(sum)
    print(t)
add()