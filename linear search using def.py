pos=0
def search(lst,a):
    for i in range(len(lst)):
        if(lst[i]==a):
            globals()['pos']=i           
            return True
      
    return False     
lst=[2,3,4,56,7,6]
a=int(input("enter a num to search"))
if search(lst,a):
    print('found in the position',pos+1)
else:
    print("not found")