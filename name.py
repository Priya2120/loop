# 1234*=24

n=int(input("enter a number :"))
i=0
m=1
while i<n:
    num=n%10
    m=m*num
    n=n//10
    i=i+1
print(m)