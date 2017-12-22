#Anđela Vanesa Tuta, 23.11.2017.
#Vjezba 5, zadatak 12


lista = []
n = int(input('Unesite pozitivan broj: '))
lista.append(n)

while n >= 0:
    n = int(input('Unesite pozitivan broj(Ukoliko zelite prekinuti unos brojeva unesite negativan) : '))
    lista.append(n)
    if n<0:
        break

suma = sum(lista)
broj = len(lista)
aritm_sredina = suma/broj

print('Aritmeticka sredina unesenih brojeva je {}'.format(aritm_sredina))