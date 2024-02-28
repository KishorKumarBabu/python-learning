num=int(input("enter starting"))
num1=int(input("enter ending"))
while num<=num1:
    for i in range(1,num):
        if(i*i==num):
            print(num)
    num+=1