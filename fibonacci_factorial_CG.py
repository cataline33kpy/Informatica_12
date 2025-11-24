def factorial_iterativ(n):
    rezultat=1
    for i in range(1, n+1):
        rezultat*=i
    return rezultat

def fibonacci_iterativ(n):
    if n<=1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a+b
    return b
n=int(input("Introduceti n pentru factorial si fibonacci: "))
print("Factorial iterativ=", factorial_iterativ(n))
print("Fibonacci iterativ=", fibonacci_iterativ(n))