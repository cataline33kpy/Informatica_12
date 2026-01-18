data_curenta=(2025, 11, 11)
produse=(
    ("Lapte", (2024, 10, 1), (2024, 12, 1), 20),
    ("Branza", (2024, 6, 1), (2025, 6, 1), 40),
    ("Iaurt", (2025, 10, 15),(2025, 11, 20),10),
    ("Carne", (2025, 9, 10), (2025, 11, 15),50),
    ("Orez", (2024, 1, 1), (2026, 1, 1), 30)
)

def in_zile(data):
    an, luna, zi=data
    return an*360+luna*30+zi


def pret_actual(data_f, data_e, pret_i):
    total=in_zile(data_e)-in_zile(data_f)
    trecut=in_zile(data_curenta)-in_zile(data_f)

    if in_zile(data_curenta)>in_zile(data_e):
        return 0, "expirat"
    elif trecut >= total * 0.75: 
        return pret_i * 0.5, "-50%"
    elif trecut >= total * 0.5: 
        return pret_i * 0.8, "-20%"
    else:
        return pret_i, "fără reducere"


expirate = []
red50 = []
red20 = []
val_1an = []
val_1luna = []

for produs in produse:
    nume, data_f, data_e, pret_i = produs
    pret, tip=pret_actual(data_f, data_e, pret_i)
    durata_zile=in_zile(data_e)-in_zile(data_f)
    
    if tip == "expirat":
        expirate.append((nume, pret))
    elif tip == "-50%":
        red50.append((nume, pret))
    elif tip == "-20%":
        red20.append((nume, pret))
    
    if durata_zile >= 360:
        val_1an.append((nume, pret))
    if durata_zile <= 30:
        val_1luna.append((nume, pret))


print("a) Produse expirate:", expirate)
print("b) Produse cu reducere 50%:", red50)
print("c) Produse cu reducere 20%:", red20)
print("d) Produse cu valabilitate ≥ 1 an:", val_1an)
print("e) Produse cu valabilitate ≤ 1 lună:", val_1luna)               