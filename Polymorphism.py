

class Add:
    def add(self, *args):
        sum = 0
        for i in args:
            sum += i
        return sum
print("This is Method Overloading")
add = Add()
print("Sum of 2 Integer Numbers = ", add.add(3, 4))
print("Sum of 2 Floating Numbers =", add.add(2.0, 4.5))
print("Sum of 3 Numbers =", add.add(6, 4, 10))

class addition(Add):
    def add(self, *args):
        sum = 10
        for i in args:
            sum += i
        return sum

Addition = addition()
print()
print("This is Method Overriding")
print("Sum of 4 Numbers =", Addition.add(2, 4, 6, 8)) 
