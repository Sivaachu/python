#Hierarichal Inheritance

class University:
    def announcement(self):
        print("New Semester Starts from Monday...!")

class Student(University):
    def submit(self):
        print("Assignment submitted by the students")


class Professor(University):
    def grade(self):
        print("Professor grade the assignment")

s1 = Student()
p1 = Professor()
s1.announcement()

s1.submit()

p1.grade()
