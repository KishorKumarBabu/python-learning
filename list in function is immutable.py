def update(lst):
    print(id(lst))
    lst[1]=25
    print(id(lst))
    print(lst)
lst=[10,20,30]
print(lst)
print(id(lst))
update(lst)
print(lst)
