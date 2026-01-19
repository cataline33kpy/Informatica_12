p = float(input("probabilitate p (0..1) = "))
n = int(input("incercari n = "))
P_succes = 1 - (1 - p) ** n
print("P =", P_succes)