#Anđela Vanesa Tuta, 23.11.2017.
#Vjezba 5, zadatak 7

n = str(input('Unesite dvoznamenkasti prirodan broj: '))
import string

if len(n) < 2 or len(n)>2:
    print('Broj nije dvoznamenkast. Ponovite unos.')
    n = str(input('Unesite dvoznamenkasti prirodan broj: '))


for i in range (10,int(n)):
    a,b = i // 10,i % 10
    if a%2 != 0:
        if b%2 != 0:
            print(i)






