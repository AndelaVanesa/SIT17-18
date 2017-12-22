#Andela Vanesa Tuta, 23.11.2017.
#Vjezba 5, zadatak 4


niz = input('Unesite niz znakova:')

import string

for i in niz:
    if i in string.ascii_letters:
        print(i)