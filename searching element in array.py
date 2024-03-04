from array import *
a=array("i",[])
n=int(input('enter the len of array'))
for i in range(n):
    x=int(input('enter the element'))
    a.append(x)
print(a)
b=int(input("enter the element to search"))
for j in range(n):
    if(b==a[j]):
        print("the search element is found in index",j)
        break
else:
     print("not found")
     