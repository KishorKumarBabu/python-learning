x=int(input("enter the num"))
def fact(n):
    a=1
    for i in range(1,n+1):
        a=i*a
    print(a)
fact(x)