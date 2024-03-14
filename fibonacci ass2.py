x=int(input("enter tn num"))
def fib(n):
    a=0
    b=1
    for i in range(n):
        print(a,end=" ")
        sum=a+b
        a=b
        b=sum
        sum=a+b
fib(x)

    