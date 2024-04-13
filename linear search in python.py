lst=[2,3,4,56,7,6]
a=int(input("enter a num to search"))
b=0
for i in lst:
    if(i==a):
        print('found in the position',b)
        break
    b+=1
else:
    print("not found")