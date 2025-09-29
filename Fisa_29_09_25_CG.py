import math
x,y=int(input("a=")),int(input("b="))
def Suma_ab(a,b):
    return a+b

def Produs_ab(a,b):
    return a*b

def Media_ab(a,b):
    return (a+b)/2

def cmmdc(a,b):
    return math.gcd(a,b)

def cmmm(a,b):
    return abs(a*b)//math.gcd(a,b)

def min_ab(a,b):
    return min(a,b)

def max_ab(a,b):
    return max(a,b)

#j)
def div_com(a,b):
    d=math.gcd(a,b)
    return[i for i in range(1,d+1) if d%i==0]

#k)
def multipl_com(a,b,n=5):
    m=abs(a*b)//math.gcd(a,b)
    return [m*i for i in range (1,n+1)]

#l)
def cifre_comune(a,b):
    return sorted(set(str(abs(a)))) and set(str(abs(b)))



def sunt_prietene(a,b):
    def nr_div(n):
        cnt=0
        for i in range(1,n+1):
            if n%i==0:
                cnt+=1
        return nr_div(a)==nr_div(b)        
print('a)Suma numerelor=',Suma_ab(x,y))
print('b)Produsul numerelor=',Produs_ab(x,y))
print('c)Media aritmetica a numerelor=',Media_ab(x,y))
print('d)Cel mai mare divizor comun=',cmmdc(x,y))
print('e)Cel mai mic multiplu comun=',cmmm(x,y))
print('f)Numarul minim=',min_ab(x,y))
print('g)Numarul maxim=',max_ab(x,y))
print('h)Suma numerelor in format=',x,'+',y,'=',Suma_ab(x,y))
print('i)Produsul numerelor in format=',x,'*',y,'=',Produs_ab(x,y))
print('j)Toti divizorii comuni=',div_com(x,y))
print('k)Cinci multipli comuni=',multipl_com(x,y))
print('l)Cifre care se contin in ambele=',cifre_comune(x,y))
print('n)Afisare prietene=',sunt_prietene(x,y))