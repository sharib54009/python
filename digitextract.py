xValueIntString=input("enter a number : ")
xint=int(xValueIntString) 
xcopy=xint
sum = 0
odd_sum = 0
even_sum = 0
while xint > 0:
   rem = xint%10
   print("extracted values are", rem)
   xint = xint//10
   sum = sum + rem
   if rem%2 == 0:
      even_sum = even_sum + rem
   if rem%2 != 0:
      odd_sum = odd_sum + rem
else: 
    print("sum of all digits is : ", sum)
    print("sum of even digits is : ", even_sum )
    print("sum of odd digits is : ", odd_sum )