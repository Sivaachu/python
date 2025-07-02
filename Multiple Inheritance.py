#Multiple Inheritance

class Person:
    def __init__(self,Name,Age):
    
        self.Name = Name
        self.Age = Age
    def display(self):
        print("Name of the Person :",self.Name)
        print("Age :",self.Age)
class Company:
    def __init__(self,Company_Name,Salary):
        self.Company_Name = Company_Name
        self.Salary = Salary
    def disp(self):
        print("Company Name :",self.Company_Name)
        print("Salar :",self.Salary)

class Employee(Person,Company):
    def __init__(self,Name,Age,Company_Name,Salary):
        Person.__init__(self,Name,Age)
        Company.__init__(self,Company_Name,Salary)
    def display1(self):
        self.display()
        self.disp()
e1 = Employee("Shiva", 21,"Tata Consultancy and Services", 300000)
e1.display1()