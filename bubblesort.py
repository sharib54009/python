<<<<<<< HEAD
list = [14, 20, 18, 9, 5, 2, 12, 23, 19, 6]
mylen = len(list)
for i in range(mylen-2, -1, -1):
    for j in range(0, i+1):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
=======
list = [14, 20, 18, 9, 5, 2, 12, 23, 19, 6]
mylen = len(list)
for i in range(mylen-2, -1, -1):
    for j in range(0, i+1):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
>>>>>>> ccf339ab26e53daabfa936e12c7d806a11bd917e
print(list)