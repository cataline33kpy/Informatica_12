def suma_cifrelor(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s
n=int(input("n = "))
m=int(input("m = "))
sume=[]
for i in range(n + 1):
    sume.append(suma_cifrelor(i))

sume.sort()
K=0
for x in sume:
    if x==m:
        K+=1

print("K =", K)