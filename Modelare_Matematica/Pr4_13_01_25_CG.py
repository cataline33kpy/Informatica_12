def termen_simulare(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    a1, a2 = 1, 2
    for _ in range(3, n + 1):
        a1, a2 = a2, a1 + a2

    return a2


n = int(input("n = "))
print("a_n =", termen_simulare(n))
