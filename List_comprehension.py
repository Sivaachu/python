#list_comprehension

lst = [1,5,8,25,26,36,39,45]

odd = [i for i in lst if i % 2 ==1]
print(odd)

even = [i for i in lst if i % 2 ==0]
print(even)

div_5 = [i for i in lst if i % 4 ==0]
print(div_5)

random = [i for i in range(0,101,4)]
print(random)