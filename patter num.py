num=int(input("enter the number :"))
i=1
while i<=num:
    j=1
    while j<=num-i:
        print(" ",end=" ")
        j=j+1
    k=1
    while  k<i:
        print(k,end=" ")
        k=k+1
    b=i
    while b>0:
        print(b,end=" ")
        b=b-1
    print()
    i=i+1
