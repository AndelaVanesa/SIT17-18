#Anđela Vanesa Tuta, 23.11.2017.
#Vjezba 5, zadatak 11


niz = str(input('Unesite proizvoljni niz znakova: '))

ascii_niz = ' '

for i in niz:

    print(ord(i)+1)

for i in niz:
    print(chr(ord(i) + 1), end ='')