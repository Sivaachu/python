#Sorting

arr = [10,5,20,9,56,45]

for i in range(len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print("Sorted array in Descending Order :",arr)


for i in range(len(arr)):
    for j in range(i):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print("Sorted array in Ascending Order :",arr)