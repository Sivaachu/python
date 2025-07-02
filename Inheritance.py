#Inheritance

class Animal:
    noLegs = 4
    def move(self):
        print("Animal is moving")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d1 = Dog()
print(d1.noLegs)
d1.move()
d1.sound()