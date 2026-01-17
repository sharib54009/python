<<<<<<< HEAD
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
 
# Test
for i in range(8):
    print(f"{i}! =", factorial(i))
=======
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
 
# Test
for i in range(8):
    print(f"{i}! =", factorial(i))
>>>>>>> ccf339ab26e53daabfa936e12c7d806a11bd917e
