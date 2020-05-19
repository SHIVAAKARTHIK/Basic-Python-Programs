class Student:
    def __init__(self,name,rollNo,marks):
        self.name = name
        self.rollNo = rollNo
        self.marks = marks
    #self works inside class level
    def info(self):
        print('Name: ',self.name)
        print('rollNo: ',self.rollNo)
        print('marks: ',self.marks)

s = Student('test',100,99);
s.info() # s object info now
