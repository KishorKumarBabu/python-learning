class a:
    def __init__(self):
        print("in a init")
    def feature1(self):
        print("feature 1-a is working")
    def feature2(self):
        print("feature 2 is working")
class b:
    def __init__(self):
        super().__init__()
        print("in b init")
    def feature1(self):
        print("feature 1-b is working")
    def feature4(self):
        print("feature 4 is working")
class c(a,b):
    def __init__(self):
        super().__init__()
        print("in c init")
    def fact(self):
        super().feature1()
        
c1=c()
c1.fact()