#Anđela Vanesa Tuta, 21.12.2017.
#Vjezba 8, zadatak 1

#a)funkcija zbroj

def zbroj (a=0,b=0):
'''
Funkcija zbroj vraća zbroj brojeva a i b
'''
    return a+b

#b)funkcija zbroj znamenaka

def zbroj_znamenaka (n):

    if n < 0:
        n*=-1
    zbroj_n = 0
    while n != 0:
        zbroj_n +=n%10
        n//10
    return zbroj_n


#c)funkcija udaljenost od 0

def udaljenost_od_0(x,y):
    d = (x**2 + y**2)**0.5
    return d




#d)funkcija udaljenost tocaka

def udaljenost_tocaka(T_1,T_2):
''''''
Vraća udaljenost između točaka T_1 i T_2 koji su uređeni parovi brojeva.
''''''
    d = math.sqrt((T_1[0]-T_2[0])**2+(T_1[1]-T_2[1]))
    return d

def main():
    T = (1,2)
    F = (1,5)

    print( udaljenost_tocaka(T,F))
    return