num=int(input("enter the number :"))
sum=0
temp=num
while num:
    f=1
    i=1
    rem=num%10
    while i<=rem:
        f=f*i
        i=i+1
    sum=sum+f
    num=num//10
if sum==temp:
    print("it is a strong number",sum)
else:
    print("it is a not strong number")













    
