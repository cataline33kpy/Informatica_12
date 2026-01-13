# a) S-a pornit dimineața de la 0 m.
H = 15
h0 = 0
u = 5
d = 3
N = max(1, (H - h0 + (u - d) - 1) // (u - d))
print("Numarul de zile1:", N)

# b) Ascensiunea începe dimineaţa de la înălţimea de 6 m.
H = 15
h0 = 6
u = 5
d = 3
N = max(1, (H - h0 + (u - d) - 1) // (u - d))
print("Numarul de zile2:", N)

# c) Ascensiunea începe odată cu căderea nopţii.
H = 15
h0 = 3
u = 5
d = 3
N = max(1, (H - h0 + (u - d) - 1) // (u - d))
print("Numarul de zile:", N)
