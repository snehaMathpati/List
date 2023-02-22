def nme():
    str=["rishabh","rishabh","abhishek","rishabh","divyashish","divyashish"]
    dup=[]
    i=0
    while i<len(str):
        if str[i] not in dup:
            dup.append(str[i])
        i=i+1
    print(dup)
nme()
