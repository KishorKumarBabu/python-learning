a=5
b=2
try:
    print("resource open")
    print(a/b)
    k=int(input("enter a num"))
    print(k)
except ZeroDivisionError as e:
    print("cannot able to divide by zero:",e)
except ValueError as e:
    print("invalid input",e)
except Exception as e:
    print("something went wrong",e)
finally:
    print("resource closed")