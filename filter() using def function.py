def is_even(n):
    return n%2==0
num=[3,2,6,8,4,6,2,9]
evens=list(filter(is_even,num))
print(evens) 