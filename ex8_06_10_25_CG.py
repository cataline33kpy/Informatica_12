import math
a,b,c=float(input('a=')),float(input('b=')),float(input('c=')),
def mediana(a,b,c):
    return (1/2)*(math.sqrt(2*b**2+2*c**2-a**2))

def afisarea_rezult(ma,mb,mc):
    print(f"m_a={ma:2f}")
    print(f"m_b={mb:2f}")
    print(f"m_c={mc:2f}")

def ex8(a,b,c):
    print('Medianele triunghiului:')
m_a=mediana(a,b,c)
m_b=mediana(b,c,a)
m_c=mediana(c,a,b)
afisarea_rezult(m_a,m_b,m_c)