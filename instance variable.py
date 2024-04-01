class car:
    def __init__(self):
        self.mil=10
        self.com='bmw'
c1=car()
c2=car()
c1.mil=8
print(c1.mil,c2.com)
print(c2.mil,c2.com)