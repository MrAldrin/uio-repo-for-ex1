
def add(x, y):
    # if x or y == str:
    #     raise ValueError('')
    return x+y

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def sin(x, N):
    taylor = 0
    for n in range(N+1):
        taylor += ((-1)**n * x**(2*n+1))/factorial(2*n+1)
    return taylor

def devide(x, y):
    return x / y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

