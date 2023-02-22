l=[1,342,75,23,98]
m=[75,23,98,12,78,10,1]
# cmn=[]
# i=0
# while i<len(l):
#     if l[i] in m:
#         cmn.append(l[i])
#     i=i+1
# print(cmn)

cmn=[]
i=0
while i<len(m):
    if m[i] not in l:
        cmn.append(m[i])
    i=i+1
print(cmn)