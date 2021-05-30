# # a=[7,5,3,2,1]
# # b=[9,8,6,4,]
# # c=a
# # print(c)
# # print(sorted(c))
# # mid = len(a+b)//2
# # res = (a[mid]+b[mid])/2
# # print("Median of list is :"+str(res))



def findMedian(a, n):
    sorted(a)
    if n % 2 != 0:
        return float(a[n // 2])
      
    return float((a[int((n-1)/2)] +
                  a[int(n / 2)])/2.0)
a = [ 1, 3, 4, 2, 7, 5, 8, 6 ]
n = len(a)
print("Median =", findMedian(a, n))