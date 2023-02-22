def uni_total(s):
    i=0
    sum=0
    while i<len(s):
        sum=sum+ord(s[i])
        i=i+1
    return sum  
a=uni_total("aaa") 
print(a)