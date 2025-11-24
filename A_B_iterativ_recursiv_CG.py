def putere_iterativ(a, b):
    rezultat=1
    for _ in range(b):
        rezultat*=a
    return rezultat

def putere_recursiv(a, b):
    if b==0:
        return 1
    return a*putere_recursiv(a, b - 1)
A=int(input("A= "))
B=int(input("B= "))

print("A^B (iterativ)=", putere_iterativ(A, B))
print("A^B (recursiv)=", putere_recursiv(A, B))