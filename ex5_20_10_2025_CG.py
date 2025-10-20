import random
n=int(input("n="))
a=[random.randint(-100,100) for _ in range(n)]
print("Vector generat:",a)
maxim=max(a)
suma=sum(x for x in a if x<maxim)
print("Elementul maxim este:",maxim)
print("Suma elementelor mai mici decat maximul:",suma)