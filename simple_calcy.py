def addition(a, b):
    return a + b
def substraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b
def division(a, b):
    if b == 0:
        return "cannot divide by 0"
    return a / b
print("simple calculator :")
print("1. addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
choice = int(input("enter your choice (1-4) : "))
num1 = float(input("enter first number :"))
num2 = float(input("enter second number :"))
if (choice != 1 or choice != 2 or choice != 3 or choice != 4):
    print("invalid choice")
elif choice == 1:
    print("result :", addition(num1, num2))
elif choice == 2:
     print("Result:", substraction(num1, num2))
elif choice == 3:
    print("Result:", multiplication(num1, num2))
elif choice == 4:
    print("Result:", division(num1, num2))
