num=int(input("enter the number"))
i=1
a=65
c=chr(a)
while i<=num:
    j=1
    while j<=num-i:
        print(" ",end=" ")
        j=j+1
    k=1
    while k<=1:
        print(c,k,c,end=" ")
        k=k+1
    b=i
    while b>1:
        print(c,b,c,end=" ")
        b=b-1
    print()
    i=i+1

# n=int(input("enter the number"))
# i=1
# charecter=65
# while charecter<=90:
#     print(charecter,chr(charecter))
#     charecter=charecter-1
#     i=i-1
#     while i<=n:
#         b=1
#     while b<=n-i:
#         print(" ",end=" ")
#         b=b+1
#     j=1
#     while j<i:
#         print(j,charecter,eend=" ")
#         j=j+1
#     k=i
#     while k>0:
#         print(k,end= " ")
#         k=k-1
#     print()
#     i=i+1    