def num():
    l=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","u","g","a","x","a"]
    i=0
    while i<len(l):
        a=l.count("a")
        b=l.count("n")
        c=l.count("t")
        d=l.count("g")
        e=l.count("u")
        f=l.count("x")
        i=i+1
    print("a -",a,"time")
    print("n -",b,"time")
    print("t -",c,"time")
    print("g -",d,"time")
    print("u -",e,"time")
    print("x -",f,"time")
    # break
num()

list=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","u","g","a","x","a"]
i=0
while i<=len(l):
    if "a" in l:
        a=l.count("a")
        b=l.count("n")
    i=i+1
print(a)
print(b)