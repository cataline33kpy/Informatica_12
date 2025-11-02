import random
for i in range(10):
    variante=[]
    while len(variante)<5:
        n = random.randint(1, 36)
        if n not in variante:
            variante.append(n)
    variante.sort()
    print(f"Varianta {i+1}: {variante}")