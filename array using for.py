from array import *
vals=array("i",[5,4,-3,2,9])
newarr=array(vals.typecode,(a for a in vals))
for i in newarr:
    print(i)