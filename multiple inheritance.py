class a:
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")
class b:
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
class c(a,b):
    def feature5(self):
        print("feature 5 is working")   
c1=c()
c1.feature1()
b1=b()
b1.feature3()