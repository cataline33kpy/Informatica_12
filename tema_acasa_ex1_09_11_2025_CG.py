elevi = [
    ("Cojocari", "Andrei", "M", 9, 10, 10),
    ("Farfa", "Maria", "F", 4, 5, 6),
    ("Paduraru", "Elena", "F", 10, 9, 9),
    ("Eminovici", "Mihai", "M", 7, 8, 7),
    ("Ivanova", "Raluca", "F", 3, 4, 5)
]

print("Media fiecarui elev:")
for e in elevi:
    medie=(e[3]+e[4]+e[5])/3
    print(f"{e[0]} {e[1]} -> media {medie:.2f}")

print("\nElevi restantieri (medie mai mica decat 5):")
for e in elevi:
    medie=(e[3]+e[4]+e[5])/3
    if medie<5:
        print(f"{e[0]} {e[1]}")

print("\nElevi eminenti (medie mai mare sau egal cu 9 si nicio nota mai mica decat 9):")
for e in elevi:
    note=e[3:6]
    medie=sum(note)/3
    if medie>=9 and min(note)>=9:
        print(f"{e[0]} {e[1]}")