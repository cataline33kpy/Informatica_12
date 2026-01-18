dictionar1 ={
    2: '56',
    1: '2',
    4: '12',
    5: '24',
    6: '18',
    3: '323'
}

valori=[]
for v in dictionar1.values():
    valori.append(int(v))

valori.sort()

for v in valori:
    print(v, end=" ")
    
dictionar2={
    2: '56',
    1: '2',
    4: '12',
    5: '24',
    6: '18',
    3: '323'
}

items=list(dictionar2.items()) 
values_num=[int(v) for _, v in items]

values_num_sorted=sorted(values_num)

rezultat=[]
for val in values_num_sorted:
    for k, v in items:
        if int(v)==val and (k, v) not in rezultat:
            rezultat.append((k, v))

print('\n',rezultat)    