# a="i am amrita"
# a=a.split()
# a="-".join(a)
# print(a)

# a="i am amrita"
# b=a.replace(" ","-")
# print(b)


# no()

l=[-3,20,61,700,-2,800,2]
# l=[-1,-6,-8]
i=0
a=l[0]
b=l[0]
while i<len(l):
    if l[i]>a:
        a=l[i]
    if l[i]<b:
        b=l[i]
    i=i+1
print(a, "max")
print(b,"min")

