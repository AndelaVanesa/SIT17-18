#Anđela Vanesa Tuta,3.11.2017.
#Vježba 2, zadatak 11


import math

#petlja za beskonačno izvođenje programa
while True:
    a = float(input("Molim, unesite a: "))
    b = float(input("Molim, unesite b: "))
    c = float(input("Molim, unesite c: "))

    #računanje determinante
    d = b ** 2 - 4 * a * c

    #provjera uvjeta
    if d < 0:
        print("Jednadžba nema realnih rješenja jer je D < 0:", round(d, 4))
    elif d == 0:
        x1 = (-b) / (2 * a)
        print("Jednadžba ima jedno dvostruko rješenje jer je D = 0:", round(x1, 4))
    elif d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("Jednadžba ima dva rješenja jer je D > 0:", round(d, 4))
        print("Rješenje x1:", round(x1, 4))
        print("Rješenje x2:", round(x2, 4))

    nastavak = input("Želite nastaviti (d/n)? ")

    if nastavak == 'n':
        break
