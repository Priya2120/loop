# guessing game.

n=1
num=5
print("what is your name")
my_name=input("enter the name")
print("hello",my_name,"i am thinkig of a number between 1 to 10")
while n<=5:
    i=int(input("enter the number"))
    n=n+1
    if i==num:
        print("guessing is correct")
        break
    else:
        print("guessing is wrong")