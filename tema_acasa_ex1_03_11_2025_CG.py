import random

#a)Adunare
a = random.randint(0, 100)
b = random.randint(0, 100)
rezultat=int(input(f"Cat face {a} + {b}? "))
if rezultat==a+b:
    print("Corect")
else:
    print(f"Gresit, raspunsul corect era {a + b}")

#b)Scadere
a = random.randint(0, 100)
b = random.randint(0, 100)
rezultat=int(input(f"Cat face {a} - {b}? "))
if rezultat==a-b:
    print("Corect")
else:
    print(f"Gresit, raspunsul corect era {a - b}")

#c)Inmultire
a = random.randint(0, 100)
b = random.randint(0, 100)
rezultat=int(input(f"Cat face {a}*{b}? "))
if rezultat==a*b:
    print("Corect")
else:
    print(f"Gresit, raspunsul corect era {a * b}")