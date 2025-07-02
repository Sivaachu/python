class Student:
    def __init__(self,__Id,Name,Age,Grade):
        self.Id = __Id
        self.Name = Name
        self.Age = Age
        self.Grade = Grade

    def getId(self,n):
        return "Id of student ",n,self.Id

    def setId(self,__Id):
        self.Id = __Id
        return __Id

s1 = Student(126,"Praveen",21,"A+")
print(s1.getId(1))


print(s1.setId(136))
print(s1.getId(1))