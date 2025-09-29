def suma(a, b, c, d):
    return a + b + c + d

def medie(i, j, k, m):
    return (i + j + k + m) / 4

def minim(a, b, c, d):
    return min(a,b,c,d)

def radacina_ec(a, b):
    if a == 0:
        return None 
    return -b / a

def cel_mai_mic_div(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i

def cmmdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def cmmmc(a, b):
    return (a * b) // cmmdc(a, b)

def ultim_nr(n):
    return n % 10

def nr_cifre(n):
    return len(str(n))

def nr_superior(n):
    return int(str(n)[0])

def nr_aparitii(sir, caracter):
    return sir.count(caracter)



a = float(input("a) Introduceti a (real): "))
b = float(input("Introduceti b (real): "))
c = float(input("Introduceti c (real): "))
d = float(input("Introduceti d (real): "))
print("a) Suma:", suma(a, b, c, d))


i = int(input("b) Introduceti i (intreg): "))
j = int(input("Introduceti j (intreg): "))
k = int(input("Introduceti k (intreg): "))
m = int(input("Introduceti m (intreg): "))
print("b) Media:", medie(i, j, k, m))
print("c) Minim:", min(a, b, c, d))
ec_a=float(input("f) Introduceti a (pentru ecuatia ax + b = 0): "))
ec_b=float(input("Introduceti b: "))
rad = radacina_ec(ec_a, ec_b)
if rad is None:
    print("f) Ecuatia nu are solutie")
else:
    print("f) Radacina:", rad)


n = int(input("g) Introduceti un numar intreg n > 0: "))
print("g) Cel mai mic divizor (≠1):", cel_mai_mic_div(n))


x = int(input("h/i) Introduceti primul numar natural: "))
y = int(input("Introduceti al doilea numar natural: "))
print("h) CMMDC:", cmmdc(x, y))
print("i) CMMMC:", cmmmc(x, y))


nr = int(input("j/k/l) Introduceti un numar intreg > 0: "))
print("j) Ultima cifra:", ultim_nr(nr))
print("k) Numar de cifre:", nr_cifre(nr))
print("l) Cifra superioara:", nr_superior(nr))


sir2 = input("m) Introduceti un sir de caractere: ")
cr = input("Introduceti caracterul de numarat: ")
print("m) Numar de aparitii:", nr_aparitii(sir2, cr))