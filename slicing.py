info ={1:"Shiva",2:"Praveen",3:"Vaishu"}

print(info)

print(info.get(1))

print(info.keys())

print(info.values())

print(len(info))

print(info.items())

info[4] = "Arya Krishna"
info[5] = "Abinaiya Sri"
print(info)

info.pop(3)
print(info)

info.clear()
print(info)

info = dict()

map = {"Name":"Shiva","Age":21,"Department":"Computer Science"}
print(map["Name"])
print(map["Age"])
print(map["Department"])

for key,value in map.items():
    print(key,":",value)