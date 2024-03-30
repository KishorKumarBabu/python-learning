class comp:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("config:",self.cpu,self.ram)
com1=comp("i5",16)
com2=comp("ryzon",16)
com1.config()
com1.config()