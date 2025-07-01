class Student:
    def __init__(self,Name,Age,Department,Marks):
        self.Name = Name
        self.Age = Age
        self.Department = Department
        self.Marks = Marks
    def display(self,n):
        print("Details of Student ",n)
        print()

s1 = Student("Shiva",21,"Computer Science",537)
print("Name :",s1.Name,"Age :",s1.Age,"Department :",s1.Department,"Marks :",s1.Marks)
s1.display(1)

s2 = Student("Praveen Kumar",20,"Computer Science",540)
print("Name :",s2.Name,"Age :",s2.Age,"Department :",s2.Department,"Marks :",s2.Marks)
s2.display(2)