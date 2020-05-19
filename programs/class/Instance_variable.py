class Student:
    '''This is for Test'''

    def __init__(self,name,marks):
        # self.name is a instace variable
        self.name = name
        self.marks= marks
    def m1(self):
        self.age = 20
    def  m2(self):
        print(self.name)
        print(self.marks)
    def m3(self):
        del self.name


s = Student('test',90)
# without calling m1 method instance variable will not create for that Object
print(s.__dict__)
s.m1()
print(s.__dict__)

s1 = Student('abc',100)
s1.m1()
s1.height = 5.5  # this is valid
print(s1.__dict__)

s2 = Student('abc',100)
s2.m1()
s2.m2()
print(s2.__dict__)


s3 = Student('abc',100)
s3.m3()
print(s3.__dict__)

s4 = Student('abc',100)
s4.m1()
print(s4.__dict__)

s5 = Student('abc',100)
s5.age = 50
print(s5.__dict__)
