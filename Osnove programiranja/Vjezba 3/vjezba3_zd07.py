#Andela Vanesa Tuta, 10.11.2017.
#Vjezba 3, zadatak 7

from math import log(x,base)

argument = float(input('Unesite argument logaritma: '))
baza = float(input('Unesite bazu logaritma: '))

while argument < 0:
    print('Neispravno unesen argument.')
    argument = float(input('Ponovo unesite argument logaritma: '))
while baza < 0 or baza == 1:
    print('Neispravno unesena baza.')
    baza = float(input('Ponovo unesite bazu logaritma: '))
else:
    print('Vrijednost logaritma sa zadanom bazom i argumentom iznosi: ', math.log(argument, baza))