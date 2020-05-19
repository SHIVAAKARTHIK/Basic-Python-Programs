class Student:
    '''This is for Test'''
    x = 10
    def __init__(self,name,marks):
        # self.name is a instace variable
        self.name = name
        self.marks= marks

s = Student('test',90)
s1 = Student('abc',100)
Student.x = 110
s.x = 100 # it wil become new instace variable for that object
print(s.__dict__)
s.name = 'lkj'
print(s.x,s.name) # 110  lkj because only one copy of Static variable will be created
print(s1.x,s1.name)
