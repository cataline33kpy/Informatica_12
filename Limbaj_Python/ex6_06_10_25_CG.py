import math
a,b,c,d=int(input('a=')),int(input('b=')),int(input('c=')),int(input('d='))
tot_perimetru=[]
toata_aria=[]
def triunghi_abc():
    global a,b,c
    return a+b>c and a+c>b and b+c>a

def triunghi_acd():
    global a,c,d
    return a+c>d and d+c>a and a+d>c

def triunghi_abd():
    global a,b,d
    return a+b>d and a+d>b and b+d>a

def triunghi_bcd():
    global b,c,d
    return b+c>d and a+d>c and c+d>b

def perimetru():
    global a,b,c,d
    if triunghi_abc():
        tot_perimetru.append((a+b+c))
    if triunghi_abd():
        tot_perimetru.append((a+b+d))
    if triunghi_acd():
        tot_perimetru.append((a+c+d))
    if triunghi_bcd():
        tot_perimetru.append((b+c+d))
    return tot_perimetru

def aria():
    global a,b,c,d
    if triunghi_abc():
        semiperimetru=(a+b+c)/2 
        toata_aria.append(math.sqrt(semiperimetru*(semiperimetru-a)*(semiperimetru-b)*(semiperimetru-c)))   
    if triunghi_abd():
        semiperimetru=(a+b+d)/2
        toata_aria.append(math.sqrt(semiperimetru*(semiperimetru-a)*(semiperimetru-b)*(semiperimetru-d))) 
    if triunghi_acd():
        semiperimetru=(a+c+d)/2
        toata_aria.append(math.sqrt(semiperimetru*(semiperimetru-a)*(semiperimetru-c)*(semiperimetru-d)))  
    if triunghi_bcd():
        semiperimetru=(b+c+d)/2
        toata_aria.append(math.sqrt(semiperimetru*(semiperimetru-b)*(semiperimetru-c)*(semiperimetru-d)))  
    return toata_aria

print(f"Toate perimetrele:{perimetru()}") 
print(f"Toate areile: {aria()}")                            