lst = [1, 33, 57, 654, 635, 6543, 23]
largest = lst[0]
for num in lst:
    if num > largest:
        largest = num
print("The largest number in the list is:", largest)