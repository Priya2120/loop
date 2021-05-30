num=int(input("enter any number"))
sum=0
i=1
while num>i:
    if num%i==0:
        sum=sum+i
        print(i)
    i=i+1
if sum==num:
    print(num,"it is perfect number")
else:
    print("it is not perfect number")