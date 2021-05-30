# num=int(input("enter the number"))
# i=1
# while i<num:
#     a=num%10
#     b=(num//10)%10
#     c=(num//10)//10
#     d=a+b+c
#     i=i+1
# if num%d==0:
#     print("it is a harshad number")
# else:
#     print("it is not harshad number")
    



i=1
while i<=1000:
    a=i%10
    b=(i//10)%10
    c=(i//10)//10
    d=a+b+c
    if i%d==0:
        print(i,"is a harshad number")
    else:
        print(i,"is not a harshad number")
    i=i+1

        
    
















