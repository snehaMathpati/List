pythonumList = []
 
 
def PythonList(start, end):
    # numlist=[]
    
    for x in range(start, end):
        numlist=[]
        if x % 2 == 0:
            numList.append(x)
    return numList
 
 
print PythonList(4, 30)
