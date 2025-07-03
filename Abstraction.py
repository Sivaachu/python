from abc import ABC,abstractmethod

class Shape(ABC):
     
    @abstractmethod
    def Area(self):
        pass

class Square(Shape):

    def __init__(self,side):
        self.side = side
        print("Side of a Square :",self.side)

    def Area(self):
        area = self.side *self.side
        return area

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        print("Length :",self.length)
        print("Breadth : ",self.breadth)
    
    def Area(self):
        area =self.length*self.breadth
        return area

class Triangle(Shape):
    def __init__(self,breadth,height):
        self.breadth = breadth
        self.height = height
        print("Breadth :",self.breadth)
        print("Height :",self.height)

    def Area(self):
        area = 1/2*self.breadth*self.height
        return area

    

    
sq = Square(5)
print("Area of Square :",sq.Area())

rec = Rectangle(10,20)
print("Area of Rectangle :",rec.Area())

tri = Triangle(10,10)
print("Area Of a Triangle :",tri.Area())