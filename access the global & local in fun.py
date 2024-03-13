a=10
def something():
    a=9
    globals()['a']=15
    print("in fun",a)
something()
print("out fun",a)
