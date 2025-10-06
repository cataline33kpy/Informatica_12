a,b=float(input('a=')),float(input('b='))
print('Introduceti numerele reale a1,...,a10:')
a1,a2,a3,a4,a5,a6,a7,a8,a9,a10=float(input()),float(input()),float(input()),float(input()),float(input()),float(input()),float(input()),float(input()),float(input()),float(input())
def maxim(x,y):
    return max(x,y)

def minim(x,y):
    return min(x,y)

S = maxim(minim(a1, a2), a3) + minim(maxim(a4, a5), minim(a6, a7))
Total = (minim(a1, a2) + minim(a3, a4) + minim(a5, a6) + minim(a7, a8) +
          minim(a9, a10) + maxim(a1, a2) + maxim(a3, a4) + maxim(a5, a6) +
          maxim(a7, a8) + maxim(a9, a10))

print("Elementul minim intre a si b =", minim(a, b))
print("Elementul maxim intre a si b =", maxim(a, b))
print("S =", S)
print("Total =", Total)