# weight question.

n=1
sum=0
while n<11:
    weight=int(input("enter the weight"))
    sum=sum+weight
    average=sum/11
    n=n+1
print(average)
if average%5==0:
    print("diviside")
else:
    print("not diviside")