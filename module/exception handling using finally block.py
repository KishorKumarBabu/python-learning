a=5
b=2
try:
    print("resource open")
    print(a/b)
except Exception as e:
    print("cannot able to divide by zero:",e)
finally:
    print("resource closed")