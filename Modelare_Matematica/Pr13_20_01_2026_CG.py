V0 = float(input("valoare initiala V0 = "))
d = float(input("depreciere d (%) = "))
n = int(input("ani n = "))
Vn = V0 * (1 - d / 100) ** n
print("Vn =", Vn)