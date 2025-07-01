rows = 5

print("1. Bottom-Left Right-Angled Triangle")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
print()

print("2. Top-Left Right-Angled Triangle")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
print()

print("3. Bottom-Right Right-Angled Triangle")
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()
print()

print("4. Top-Right Right-Angled Triangle")
for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()