a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))

def add():
     c = a + b
     print("The Sum of a and b is",c)
add()

def sub():
    d = a - b
    print("The Difference of a and b is",d)
sub()

def mul():
    f = a*b
    print("The Product of a and b is",f)
mul()

def div(p,s):
    e = p/s
    print("The Quotient of a and b is",e)
div(10,5)

def mod(g,h):
    m = g % h
    print("The Remainder of a and b is",m)
mod(10,3)

def floor():
    l = a//b
    print("Floor Divison of a and b is",l)
floor()

def exp():
    ex = a**b
    print("Exponent of a and b is",ex)
exp()

