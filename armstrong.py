num = int(input("enter a 3 digit number : "))
sum = 0
temp = num
while temp > 0 :
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if sum == num :
    print (sum, "is an armstrong")
else :
    print (sum, "is not an armstrong")  