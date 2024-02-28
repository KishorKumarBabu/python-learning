x=int(input("enter a number to check prime or not"))
for i in range(2,x):
    if(x%i==0):
        print("not prime number")
        break
else:
    print("prime number")