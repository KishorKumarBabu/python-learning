from numpy import *
arr=array([1,2,3,4,5])
arr1=array([1,2,3,4,5])
for i in range(5):
    arr[i]=arr[i]+arr1[i]
print(arr)