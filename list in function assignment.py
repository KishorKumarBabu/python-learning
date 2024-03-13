list=[]
def count(list):
    greater=0
    lower=0
    for i in list:
        x=len(i)
        if x>5:
            greater+=1
        else:
            lower+=1
    return greater,lower
for i in range (5):
    lst=input("enter name")
    list.append(lst)
greater,lower=count(list)
print("greater:{} and lower:{}".format(greater,lower))