# code likho 30 se 420 tak ke unn numbers ka sum culcuulate ho jo 8 ke multiple hai yaani 
# wo numbers ke table (paahade) mein aate hai.

n=30
sum=0
while n<=420:
    if n%8==0:
        sum=sum+n
        print(n,sum)
    n=n+1