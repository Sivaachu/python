class Employee:
    def __init__(self,Name,salary):
        self.Name = Name
        self.salary = salary
    def get_details(self):
        print("Name of the Employeer:",self.Name)
        print("Salary :",self.salary)
class manager(Employee):
    def __init__(self,Name,salary,bonus):
        super().__init__(Name,salary)
        self.bonus = bonus
    def calculate(self):
        bonus1 = self.bonus + self.salary
        return bonus1

m1 = manager("Shiva",10000,2500)
m1.get_details()
print("Bonus :",m1.bonus)
print("Bonus :",m1.calculate())
