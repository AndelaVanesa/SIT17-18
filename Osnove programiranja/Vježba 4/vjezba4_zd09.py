#Anđela Vanesa Tuta, 16.11.2017.
#Vježba 4, zadatak 12

niz = input('Unesite niz znakova: ')
lista = list(niz)

praznine = lista.count(' ')
print('U unesenom nizu znakova se nalaze/i', praznine, 'praznine/a.')

lista.sort()
print(lista)

del lista[-1]
print(lista)

if 'a' in lista:
    print('Znak a se nalazi u listi.')
    lista.remove('a')
    print(lista)
else:
    print('Znak "a" se ne nalazi u listi.')