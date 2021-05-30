# 101010 print:

i=7
while i>=1:
    k=6
    while k>=i:
        print("",end=" ")
        k=k-1
    j=1
    while j<=i:
        if j%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
        j=j+1
    i=i-2
    print()