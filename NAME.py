name=input("enter a name :")
i=0
while i<len(name):
    print(name.upper()[i]+name.lower()[i]*(i),end="")
    if i!=len(name)-1:
        print("_",end="")
    i=i+1
