u=int(input("enter the no."))
i=1
m=0
while i<=u: 
    if i%u==0 and u==m:
        m=m+i
        print(m,"is perfect no")
    else :
        print(m,"is not perfect no.")
        # break
    i=i+1
