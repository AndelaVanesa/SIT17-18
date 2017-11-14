#Andela Vanesa Tuta, 10.11.2017.
#Vjezba 3, zadatak 4

bodovi = int(input('Unesite broj postignutih bodova: '))
while bodovi > 100 or bodovi < 0:
    print('Pogrešan unos.')
    bodovi = int(input('Ponovo unesite broj bodova: '))
if 0<= bodovi <= 59:
    print('Ocjena prema broju bodova je nedovoljan (1)')
elif 60 <= bodovi <= 69:
    print('Ocjena prema broju bodova je dovoljan (2)')
elif 70 <= bodovi <= 79:
    print('Ocjena prema broju bodova je dobar (3)')
elif 80 <= bodovi <= 89:
    print('Ocjena prema broju bodova je vrlo dobar (4)')
else:
    print('Ocjena prema broju bodova je odličan (5)')