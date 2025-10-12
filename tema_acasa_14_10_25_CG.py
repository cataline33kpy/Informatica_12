baza = 0  

b = int(input("Introduceți baza (între 2 și 9): "))
a = input("Introduceți primul număr: ")
c = input("Introduceți al doilea număr: ")

def seteaza_baza(b):
    global baza
    if 1<b<10:
        baza=b
        print(f"\n Baza a fost setată la {baza}.")
    else:
        print("Baza trebuie să fie între 2 și 9.")

def este_valid(numar):
    global baza
    for cifra in str(numar):
        if int(cifra)>=baza:
            return False
    return True

def converteste(numar, din_baza, in_baza):
    numar10=0
    putere=1
    for cifra in str(numar)[::-1]:
        numar10+=int(cifra)*putere
        putere *= din_baza
    rezultat = ""
    while numar10 > 0:
        rezultat=str(numar10 % in_baza)+rezultat
        numar10 //= in_baza
    return rezultat or "0"

def aduna(x, y):
    global baza
    if not (este_valid(x) and este_valid(y)):
        return "Număr invalid pentru baza dată."
    s=int(converteste(x, baza, 10))+int(converteste(y, baza, 10))
    return converteste(s, 10, baza)

def scade(x, y):
    global baza
    if not (este_valid(x) and este_valid(y)):
        return "Număr invalid pentru baza aceasta."
    s=int(converteste(x, baza, 10))-int(converteste(y, baza, 10))
    if s<0:
        return "Rezultatul este negativ, nu poate fi reprezentat în baza aceasta."
    return converteste(s, 10, baza)

def inmulteste(x, y):
    global baza
    if not (este_valid(x) and este_valid(y)):
        return "Număr invalid pentru aceasta baza."
    p=int(converteste(x, baza, 10))*int(converteste(y, baza, 10))
    return converteste(p, 10, baza)

seteaza_baza(b)
print(f"\nNumerele: {a} și {c} (în baza {baza})")
print(f"Validare {a}: {este_valid(a)}")
print(f"Validare {c}: {este_valid(c)}")
print(f"\nSuma = {aduna(a, c)} (baza {baza})")
print(f"Diferența = {scade(a, c)} (baza {baza})")
print(f"Produsul = {inmulteste(a, c)} (baza {baza})")