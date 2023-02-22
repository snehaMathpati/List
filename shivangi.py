elements=[23,14,56,12,19,9,15,25,31,42,43]
n=len(elements)
i=0
sum=0
while i<len(elements):
    j=0
    while j<len(elements):
        sum=sum+elements[i][j]
        j=j+1
        print(sum)
    ave=sum/len(elements[i])
    i=i+1
    print(ave)