num=[3,2,6,8,4,6,2,9]
evens=list(filter(lambda n:n%2==0,num))
doubles=list(map(lambda n:n*2,evens))
print(evens) 
print(doubles)