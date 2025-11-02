import random
while True:
    n = random.randint(100, 999)
    if n%24==0:
        print("Numar generat:", n)
        break