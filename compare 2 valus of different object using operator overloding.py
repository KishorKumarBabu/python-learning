class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __gt__(self,other):
        s1=self.m1+self.m2
        s2=other.m1+other.m2
        if(s1>s2):
            return True
        else:
            return False
s1=student(50,80)
s2=student(50,90)
if(s1>s2):
    print("s1 wins")
else:
    print("s2 wins")