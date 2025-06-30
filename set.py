set1 = {10,20,30,40}
print(set1)

#To add an element in a set
set1.add(9)
set1.add(True)
print(set1)

#To remove an element
set1.remove(20)
set1.remove(1)
print(set1)

#To delete all elements in a list
set1.clear()
print(set1)

#to convert a list or tuple into set
lst = [10,30,20,50,60,80]
set10 = set(lst)
print(set10)

tup = ("Apple","Banana","Citrus","Guava","Pomegranate")
set2 = set(tup)
print(set2)

#Set Operations

Set_A = {10,20,30,40}
Set_B = {50,60,20,10}

print(Set_A.union(Set_B))

print(Set_A.intersection(Set_B))

print(Set_A.difference(Set_B))
print(Set_B.difference(Set_A))

for i in Set_A:
    print(i)