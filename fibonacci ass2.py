x=int(input("enter tn num"))
def fib(n):
    a=0
    b=1
    if(x<0):
        print("invalid")
    else:   
        for i in range(n):
            if(a<=n):
                print(a,end=" ")
                sum=a+b
                a=b
                b=sum
                
fib(x)

    