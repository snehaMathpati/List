def add (a,b):
    c=a+b
    return c
def mul (d,e):
    f=d*e
    return f
def main():
    symb=int(input("enter smbl"))
    if symb=="+":
        print(add(2,3))
        print(mul(3,6))
main()
