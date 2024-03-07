from numpy import *
arr=array([1,2,3,4,5])
arr1=arr.view()

print(arr)
print(arr1)
print(id(arr))
print(id(arr1))