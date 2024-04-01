class computer:
    def __init__(self):
        self.name="kishor"
        self.age=20
    def update(self):
        self.age=18
    def compare(self,other):
        if(self.age==other.age):
            return True
        else:
            return False
c1=computer()
c1.update()
c2=computer()
if c1.compare(c2):
    print("same")
else:
    print("different")
print(c1.age)
print(c2.age)