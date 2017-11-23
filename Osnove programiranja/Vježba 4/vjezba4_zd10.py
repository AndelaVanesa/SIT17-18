#Andela Vanesa Tuta, 16.11.2017.
#Vjezba 4, zadatak 10

a = input('Unesite prvo ime: ')
b = input('Unesite drugo ime: ')
c = input('Unesite treće ime: ')
d = input('Unesite četvrto ime: ')
e = input('Unesite peto ime: ')

lista = [a, b, c, d, e]
lista.sort()
print('\n'.join(lista))

for i in range(1, 6):
    print(i, '.', lista[i-1:i])