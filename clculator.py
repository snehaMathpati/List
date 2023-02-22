# def add(a,b):
#     c=a+b
#     return c
# def sub(a,b):
#     d=a-b
#     return d
# def mul(a,b):
#     e=a*b
#     return e
# def div(a,b):
#     f=a/b
#     return f
# def main():
#     if sym=="+":
#         print("total=",add(a,b))
#     elif sym=="-":
#         print(sub(a,b))
#     elif sym=="*":
#         print(mul(a,b))
#     else:
#         print(div(a,b))
# a=int(input("enter the no."))
# sym=(input("enter the sym."))
# b=int(input("enter the no."))
# main()

def add(a,b):
    c=a+b
    return c
def sub(a,b):
    z=a-b
    return z
def main():
    if sym=="+":
        print("total=",add(a,b))
    if sym=="-":
        print("total=",sub(a,b))
a=int(input("enter the no..:"))
sym=input("enter the sym")
b=int(input("enter the no..:"))
main()
