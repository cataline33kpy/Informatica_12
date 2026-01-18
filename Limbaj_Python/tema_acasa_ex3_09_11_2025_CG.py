persoane = [
    (17, 160, 50, "F", "necasatorit"),
    (25, 175, 70, "M", "casatorit"),
    (30, 165, 60, "F", "necasatorit"),
    (19, 180, 75, "M", "necasatorit"),
    (40, 172, 80, "F", "casatorit")
]

n=len(persoane)
media_greutate=sum(p[2] for p in persoane)/n
sub20=sum(1 for p in persoane if p[0]<20)/n*100
inalt170=sum(1 for p in persoane if p[1]>170)/n*100
mase18=[p[2] for p in persoane if p[0]>18]
media18=sum(mase18)/len(mase18)

femei20 = sum(1 for p in persoane if p[3]=="F" and p[0]>20 and p[4]=="necasatorit")/n*100
intre2050=sum(1 for p in persoane if 20<=p[0]<=50 and p[2]>media_greutate)/n*100

print(f"Procent sub 20 ani: {sub20:.2f}%")
print(f"Procent inaltime>170 cm: {inalt170:.2f}%")
print(f"Masa medie>18 ani: {media18:.2f} kg")
print(f"Procent femei>20 ani necasatorite: {femei20:.2f}%")
print(f"Procent 20 si 50 ani cu greutate > medie: {intre2050:.2f}%")