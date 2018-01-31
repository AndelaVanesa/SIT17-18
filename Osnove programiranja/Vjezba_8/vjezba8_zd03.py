#Anđela Vanesa Tuta, 21.12.2017.
#Vježba 8, zadatak 3


def kvadrant(x,y):
    if x > 0 and y > 0:
        return 'I kvadrant'
    elif x < 0 and y > 0:
        return 'II kvadrant'
    elif x < 0 and y < 0:
        return 'III kvadrant'
    elif x > 0 and y < 0:
        return 'IV kvadrant'
    elif x == 0 and y != 0:
        return 'Točka se nalazi na osi y'
    elif x != 0 and y == 0:
        return 'Točka se nalazi na osi x'
    else:
        return 'Točka se nalazi u ishodištu'

x,y = int(input('Unesite x: ')),int(input('Unesite y: '))
print(kvadrant(x,y))
