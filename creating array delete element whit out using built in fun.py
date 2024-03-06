from array import *
a=array("i",[])
n=int(input('enter the len of array'))
for i in range(n):
    x=int(input('enter the element'))
    a.append(x)
print(a)
for d in range(n):
    if d==2:
        a.pop(d)
print(a)