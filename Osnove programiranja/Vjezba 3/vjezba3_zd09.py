#Anđela Vanesa Tuta, 10.11.2017.
#vjezba 3, zadatak 9

from string import *

slovo = input('Unesite slovo: ')


if slovo in ascii_lowercase:
    print('To je malo slovo.')
    print('Odgovarajući ASCII kod je ', ord(slovo))
elif slovo in ascii_uppercase:
    print('To je veliko slovo.')
    print('Odgovarajući ASCII kod je ', ord(slovo))

else:
    print('Ovo nije slovo engleske abecede.')
