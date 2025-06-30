#Functions

def reverse(n):
    rev = 0
    while n>0:
        rem = n % 10
        rev = rev * 10 + rem
        n=n//10
    print("Reversed number is",rev)
reverse(231)

def reversed(n):
    return int(str(n)[::-1])

print("Reveresed number is",reversed(1234))
