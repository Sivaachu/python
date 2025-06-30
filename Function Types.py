#Function Types

#void function
def msg():
    name = input("Enter your name : ")
    print("Good morning",name)
msg()

#non void function
num = int(input("Enter a number : "))
def OddEven(num):
    
    if num % 2 == 0:

        return "Even"
    else:
        return "Odd"
result = OddEven(num)
print(num,"is",result)

#Function without Paramter
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
def add():
    c = a+b
    print("Sum = ",c)
add()

#Function with Paramter

def mul(p,s):
    return p*s
product = mul(10,2)
print("The product is",product)
