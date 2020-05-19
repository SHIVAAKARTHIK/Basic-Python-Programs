class Student:
    '''This is for Test'''
    #constructor
    #self is pointing to the current object
    # name of constructor always __init__
    def __init__(self,name,age,marks):
        print(type(self)) #'__main__.Student'
        print(id(self))
        # self.name is a instace variable
        self.name = name
        self.age = age
        self.marks= marks
        print(type(self.name),type(self.age))



s = Student('test',9,90)
print(type(s.name))
print(type(s.age))
#print(id(s))
