from array import *
vals=array("i",[5,4,-3,2,9])
newarr=array(vals.typecode,(a*a for a in vals))
i=0
while i<len(newarr):
    print(newarr[i])
    i+=1