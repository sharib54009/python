 
num = int(input("enter a number : "))
reversed = 0
numinput = num
while num > 0:
    digit= num%10
    reversed = reversed*10 + digit
    num=num//10 
if numinput == reversed  :
    print("Its a pallindrome")
else:
    print("Not a pallindrome")