#Andela Vanesa Tuta
#Vjezba 12, zadatak 1

import random
n = int(input('Unesite cijeli broj veći od 0: '))

while n <= 0:
    print('Uneseni broj mora biti biti veći od 0.')
    n = int(input('Ponovite unos: '))

lista = []
p = 0
nep = 0


for i in range(n):
    lista.append(random.randint(1, 100))

for j in lista:
    if j%2==0:
        p+=1
    else:
        nep+=1
print(lista)
print('Ima {0} parnih i {1} neparnih brojeva.'.format(p,nep))


