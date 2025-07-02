#Multilevel Inheritance

class Shape:
    def __init__(self):
        print("Shape Initialized..!")

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class Cuboid(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height
    def volume(self):
        return self.area() * self.height

cuboid = Cuboid(2,3,4)

print("Length :",cuboid.length)
print("Width :",cuboid.width)
print("Height :",cuboid.height)
print("Area :",cuboid.area())
print("Volume :",cuboid.volume())