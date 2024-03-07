from numpy import *
arr=array([1,2,3,4,5])
arr1=0
for i in range(5):
    if(arr[i]>arr1):
        arr1=arr[i]
print(arr1)