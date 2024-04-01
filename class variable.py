class car:
    wheel=4
    def __init__(self):
        self.mil=10
        self.com='bmw'
c1=car()
c2=car()
c1.mil=8
car.wheel=5
print(c1.mil,c2.com,c1.wheel)
print(c2.mil,c2.com,c2.wheel)