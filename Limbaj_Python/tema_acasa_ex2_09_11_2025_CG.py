data_curenta=(9, 11, "Duminica")
zile_sapt=("Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica")
zile_luna=(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
zile_trecute=sum(zile_luna[:data_curenta[1]-1])+data_curenta[0]
poz=zile_sapt.index(data_curenta[2])
nr_zile_aceeasi=0
for i in range(zile_trecute):
    zi_sapt=zile_sapt[i%7]
    if zi_sapt==data_curenta[2]:
        nr_zile_aceeasi+=1

print(f"Data curenta: ziua {data_curenta[0]} luna {data_curenta[1]} ({data_curenta[2]})")
print(f"Pana azi au fost {nr_zile_aceeasi} zile de {data_curenta[2]} in acest an.")