import random
n=int(input('n='))
sp=0
sn=0
for i in range(n):
    x=random.randint(-50,50)
    print(x,end='   ')
    if x>0:
        sp+=x
    elif x<0:
        sn+=x

print('\n Suma valorilor pozitive:',sp)
print('Suma valorilor negative:',sn)