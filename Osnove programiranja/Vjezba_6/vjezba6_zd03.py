#Anđela Vanesa Tuta, 30.11.2017.
#Vjezba 6, zadatak 3

m = int(input('Unesite neki prirodan broj m: '))
n = int(input('Unesite neki prirodan broj n: '))

while m <= 0:
    m = int(input('m mora biti veći od 0. Ponovite unos:'))
while n <= 0:
    n = int(input('n mora biti veći od 0. Ponovite unos:'))


i = 1
lista = []
if m <= n:
    for i in range(2, m + 1):
        if m % i == 0 and n % i == 0:
            lista.append(i)
            i += 1
else:
    for i in range(2, n + 1):
        if m % i == 0 and n % i == 0:
            lista.append(i)
            i += 1
print(min(lista))
