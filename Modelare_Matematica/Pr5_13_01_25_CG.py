def zile_pana_la_varf(H, u, d, h0, incepe_dimineata=True):
    zi=0
    h=h0
    while h<H:
        zi+=1
        if incepe_dimineata or zi>1:
            h+=u
            if h>=H:
                break
        h-=d
        if h<0:
            h=0

    return zi


#a)Incepe dimineata de la 0m
H=15
u=5
d=3
h0=0

rezultat_a = zile_pana_la_varf(H, u, d, h0, incepe_dimineata=True)
print("a)Buburuza ajunge in varf in", rezultat_a, "zile")


#b)Incepe dimineata de la 6m
h0=6

rezultat_b=zile_pana_la_varf(H, u, d, h0, incepe_dimineata=True)
print("b)Buburuza ajunge in varf in", rezultat_b, "zile")


# c)Incepe noaptea de la 6m
rezultat_c = zile_pana_la_varf(H, u, d, h0, incepe_dimineata=False)
print("c)Buburuza ajunge in varf in", rezultat_c, "zile")
