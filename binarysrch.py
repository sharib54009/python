list = [14, 20, 18, 9, 5, 2, 12, 23, 19, ]
mylen = len(list)
for i in range(mylen-2, -1, -1):
    for j in range(0, i+1):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
sEle = 5
min = 0
max = len(list) - 1  
for i in range (len(list)):
    mid = (min + max)//2
    if [mid] == sEle:   
        print(mid)
     
