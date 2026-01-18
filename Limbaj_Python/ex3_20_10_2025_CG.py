import random
nr=random.randint(0,999999999)
print('Numarul generat este:',nr)
sir=str(nr)
for cifra in range(10):
    print(f"Cifra {cifra} apare de {sir.count(str(cifra))} ori")