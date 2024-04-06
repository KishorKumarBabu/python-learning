class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        s1=self.m1+other.m1
        s2=self.m2+other.m2
        s3=student(s1,s2)
        return s3
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)
        
s1=student(50,80)
s2=student(50,20)
s3=s1+s2
print(s1)
