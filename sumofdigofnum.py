num = int(input("enter the number: "))
sum = 0
numcopy = num
while numcopy > 0:
    rem = num%10
    numcopy = numcopy//10
    sum = sum + rem
print("sum of digits of the number", num, "is:", sum)