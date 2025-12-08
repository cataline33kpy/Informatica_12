v=int(input('Volumul maxim al rucsacului: '))
n=int(input('Numarul de obiecte: '))
p=[int(input('Care e pretul unui obiect?: ')) for i in range(n)]
vn=[int(input('Care e volumul unui obiect?: ')) for i in range(n)]
x=[0]*n
i=0
vt=0
pt=0

while vt<v and i<n:
    if vt+vn[i]<=v:
        x[i]=1
        vt=vt+vn[i]
        pt=pt+p[i]*x[i]
    i+=1

print('Pretul total:', pt)
print('Volumul ocupat:', vt)
print('In rucsac s-au pus:')

for i in range(n):
    if x[i]>0:
        print('Obiectul',i+1,'(',vn[i]*x[i],',',p[i],')')