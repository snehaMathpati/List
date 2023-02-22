def kbc():
    qtn=["How many continents are there ?","What is the capital of India ?",
    "NG mei kaun se course padhaya jaata hai ? "]

    opt=[["Four","Nine","Seven","Eight"],
    ["Chandigarh","Bhopal","Chennai","Delhi"],
    ["Software Engineering","Counseling","Tourism",
    "Agriculture"]]
    slt=[3,4,1]
    L_line=[["Seven","Eight"],["Bhopal","Delhi"],["Software Engineering","Counseling"]]
    sltn=[0,1,0]
    i=0
    while i<len(qtn):
        print("Q.",i+1,qtn[i])
        print(opt[i])
        print("if you want 5050 life line then enter life_line_5050 or enter your number.")
        j=0
        while j<len(qtn):
            # ur=input("enter the 5050 life line")
            # if ur=="life_line_5050":
            def fty():
                u=input("enter the no.")
                if u=='5050':
                    print(L_line[0])
                elif u==slt[i]:
                    print("congrats..! you won.")
                else:
                    print("sorry..! you loos the game")
                def ftyy():
                    a=int(input("enter the no."))
                    if a==sltn[i+1]:
                        print("you are correct")   
                ftyy()
            fty()
        i=i+1
kbc()