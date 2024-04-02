class student:
    def __init__(self,name,reg):
        self.name=name
        self.reg=reg
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.reg)
        self.lap.show()
    class laptop :
        def __init__(self):
            self.brand="hp"
            self.cpu="i5"
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)
s1=student("kishor",3)
s2=student("loke",4)
s1.show()
lap1=student.laptop()