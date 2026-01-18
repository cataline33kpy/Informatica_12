import random
n=int(input('De cate ori se arunca zarul:'))
valori=[1,2,3,4,5,6]
aparitii=[0]*6
for i in range(n):
    fata=random.choice(valori)
    aparitii[fata-1]+=1
    
for i in range(6):
    print(f"Valoarea{i+1} a aparut de {aparitii[i]} ori")