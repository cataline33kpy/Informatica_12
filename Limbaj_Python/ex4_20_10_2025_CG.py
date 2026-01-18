import random
aruncari=0
while True:
    zar1=random.randint(1,6)
    zar2=random.randint(1,6)
    aruncari+=1
    print(f"Aruncarea{aruncari}: {zar1},{zar2}")
    if zar1==zar2:
        print(f"S-a obtinut dubla {zar1} dupa {aruncari} aruncari")
        break