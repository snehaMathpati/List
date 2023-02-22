# 22.What is the output of the following code snippet?o/p=4 4
num = 1
def func():
    global num
    num = num + 3
    print(num)

func()
print(num)
