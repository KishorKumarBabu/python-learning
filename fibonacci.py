n=50
a=0
b=1
sum=a+b
count=1
while count<=n:
    count+=1
    print(a,end="")
    a=b
    b=sum
    sum=a+b
    
    