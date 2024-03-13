def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('kishor',age=18,place='chinnamottur',mob=960081)
