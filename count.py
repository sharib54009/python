list = [1, 1, 2, 2, 2, 3, 4, 5]
dict = {}
for x in list :
    if x in dict:
        print(f" {x} -> item exist")
        dict[x] += 1
    else :
       print(f" {x} -> item does not exist")
       dict[x]=1


print(dict)
