#Anđela Vanesa Tuta, 10.11.2017
#vjezba 3, zadatak

from math import sqrt

 #Korisnik unosi duljine stranica trokuta
a= float(input('Unesite duljinu stranice a:'))
b= float(input('Unesite duljinu stranice b:'))
c= float(input('Unesite duljinu stranice c:'))
s=(a+b+c)/2

#Provjeravamo da li te stranice sačinjavaju trokut

if (a+b)<c or (a+c)<b or (b+c)<a:
    print('Stranice ne mogu sačinjavati trokut.')
    a = float(input('Unesi duljinu stranice a: '))
    b = float(input('Unesi duljinu stranice b: '))
    c = float(input('Unesi duljinu stranice c: '))
elif (a+b)>c and (a+c)>b and (b+c)>a:
    s= (a+b+c)/2
    P= sqrt(s*(s-a)*(s-b)*(s-c))
    print('Površina trokuta iznosi {}.'.format(P))
