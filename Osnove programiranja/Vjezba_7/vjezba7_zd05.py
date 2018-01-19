#Anđela Vanesa Tuta , 7.12.2017.
#Vjezba 7, zadatak 4

niz = str(input('Unesite niz znakova: '))
lista = list(niz)
lista = lista.sort()

while ',' in lista:
    lista = lista.remove(',')
while '.' in lista:
    lista = lista.remove('.')
print(lista)