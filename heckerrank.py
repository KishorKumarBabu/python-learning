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

# print function
n = int(input())
for i in range(1,n+1):
    print(i,end="")
    
#list comparision

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    i1=[_ for _ in range(x+1)]
    j1=[_ for _ in range(y+1)]
    k1=[_ for _ in range(z+1)]
    l=[]
    for i in i1:
        for j in j1:
            for k in k1:
                if(i+j+k !=n):
                    l.append([i,j,k])
                    
print(l)  

#nested list

if __name__ == '__main__':
    arr=[]
    tempscores=[]
    result=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
        tempscores.append(score)
    tempscores=list(set(tempscores))
    tempscores.sort()
    secondlowestvalue=tempscores[1]
    for i in range(len(arr)):
        if(arr[i][1] == secondlowestvalue):
            result.append(arr[i][0])
    result.sort()        
    for i in result:
        print(i)  
        
#runner up sdore

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    for i in range(n):
        if arr[i] > arr[i+1]:
            print(arr[i+1])
            break
            a  