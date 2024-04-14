pos=0
def search(lst,a):
    l=0
    u=len(lst)-1
    while (l<=u):
        mid=(l+u)//2
        if lst[mid]==a:
            globals()['pos']=mid
            return True
        else:
            if lst[mid]<a:
                l=mid+1
            else:
                u=mid-1
    return False     
lst=[2,3,4,5,6,7,8,9]
a=int(input("enter a num to search"))
if search(lst,a):
    print('found in the position',pos+1)
else:
    print("not found")