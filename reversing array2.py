from array import *
arr=array("i",[1,2,3,4,5])
len=len(arr)
arr1=array(arr.typecode,[])
i=1
while i<=len:
    arr1.append(arr[len-i])
    i+=1
print(arr1)
    