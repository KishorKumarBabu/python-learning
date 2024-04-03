class a:
    def __init__(self):
        print("in a init")
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")
class b(a):
    def feature3(self):
        print("feature 3 is working")
b1=b()
