#Andela Vanesa Tuta
#Loto 7/39

import random

def izvlacenje_brojeva():
    lista2 = [0] * 7
    for i in range(7):
        while True:
            n = random.randint(1, 40)
            if n not in lista2:
                lista2[i] = n
                break
    return lista2

def usporedba(lista1, lista2):
    br=0
    for i in range(len(lista1)):
        if lista1[i] in lista2:
            br += 1
    return br


def main():

    lista1 = list([0] * 7)
    kraj_igre = 0
    
    for i in range(7):
        while True:
            n = int(input('Upisite {}. broj od 1 do 39: '.format(i+1)))
            if n not in lista1 and n > 0 and n < 40:
                lista1[i] = n
                break
            elif n == 0:        
                kraj_igre = 1
                break
        if kraj_igre:
            break

    if not kraj_igre:
        lista2 = izvlacenje_brojeva()
        pog = usporedba(lista1, lista2)
        if pog == 7:
            print('JACKPOT!!!')
        else:
            print('Pogodili ste {} brojeva'.format(pog))

        izv = izvlacenje_brojeva()
        print('Izvučeni brojevi su {}'.format(izv))
    else: 
        print("KRAJ IGRE")

main()

