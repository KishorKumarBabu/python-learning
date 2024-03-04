from array import *
a=array("i",[])
n=int(input('enter the len of array'))
for i in range(n):
    x=int(input('enter the element'))
    a.append(x)
print(a)
b=int(input("enter the element to search"))
for i in range(n):
    if(b==a[i]):
        print("the search element is found in index",i)
        break
else:
     print("not found")
     