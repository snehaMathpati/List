# i=5
# while i>=1:
#     print()
#     j=1
#     while j<=i:
#         print("*",end=' ')
#         j=j+1
#         # print()
#     i=i-1

# a=['a','b','c','d','e','f','g','h','i','j']
# i=0
# s=1
# while i<len(a):
#     # s=s+i
#     print(a[i])
#     s=s+i
#     i=i+2
    

a=[[2,3],[4,1]]
i=0
while i<len(a):
    j=0
    s=0
    b=0
    while j<len(a[i]):
        s=s+a[i][j]
        b=b+s
        j=j+1
    i=i+1
print(b)

# a=[2,3,1,2]
# i=0
# s=0
# while i<len(a):
#     s=s+a[i]
#     i=i+1
# print(s)