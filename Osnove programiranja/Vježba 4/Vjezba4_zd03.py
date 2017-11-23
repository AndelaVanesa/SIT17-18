#Anđela Vanesa Tuta, 16.11.2017.
#Vježba 4, zadatak 3

niz = input('Unesite niz znakova: ')
n = int(input('Unesite cijeli broj: '))

if str(n+1) in niz:
    print('Broj',n+1,' se nalazi u nizu '+niz)
else:
    print('Broj',n+1,' se NE nalazi u nizu  '+niz)