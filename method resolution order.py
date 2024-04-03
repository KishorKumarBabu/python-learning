class a:
    def __init__(self):
        print("in a init")
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")
class b:
    def __init__(self):
        super().__init__()
        print("in b init")
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
class c(a,b):
    def __init__(self):
        super().__init__()
        print("in c init")
c1=c()