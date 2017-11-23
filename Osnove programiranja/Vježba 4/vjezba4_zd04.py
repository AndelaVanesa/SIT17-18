#Andela Vanesa Tuta, 16.11.2017.
#Vjezba 4, zadatak 4

niz = input('Unesite niz znakova: ')

niz1 = niz[::3]
niz2 = niz1.replace('', ' ')
print(niz2.strip())