
def factorial(num1):
    res = 1
    i = 1
    while i <= num1:
        res *= i
        i = i + 1
    print("Factorial of ", num1, " is ", res)
    
factorial(5)