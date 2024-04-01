class computer:
    def __init__(self):
        self.name="kishor"
        self.age=20
    def update(self):
        self.age=18
c1=computer()
c2=computer()
c1.age=29
c1.update()
print(c1.age)
print(c2.age)