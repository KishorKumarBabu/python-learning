# add mul sob

a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)

#devision
a = int(input())
b = int(input())
print(a//b)
print(a/b)

#sqrt
n = int(input())
for i in range(n):
    a=i*i
    print(a)
    
#leap
def is_leap(year):
    if year==2100:
        leap=False
    elif year%4==0:
        leap = True
    elif year%4==0:
        leap=False
    else:
        leap=False
    
    return leap

year = int(input())
print(is_leap(year))
