import math

def arie_triunghi(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def afiseaza_laturi(a, b, c):
    print(f"\nLaturile triunghiului sunt: a={a}, b={b}, c={c}")

def ex9(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print("\nNu se poate forma un triunghi cu aceste laturi!")
        return

    A = arie_triunghi(a, b, c)

    h_a = 2 * A / a
    h_b = 2 * A / b
    h_c = 2 * A / c
    afiseaza_laturi(a, b, c)
    print(f"Aria triunghiului = {A:.2f}")
    print(f"h_a = {h_a:.2f}")
    print(f"h_b = {h_b:.2f}")
    print(f"h_c = {h_c:.2f}")

print("Calculul ariilor și înălțimilor triunghiului")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))