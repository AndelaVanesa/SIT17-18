#Andela Vanesa Tuta, 23.11.2017.
#Vjezba 5, zadatak 6

n = int(input('Unesite broj ocjena: '))

zbroj = 0
prosjek = zbroj/n

for i in range (1,n+1):
    ocjena = int(input('Unesite ocjenu od 1 do 5: '))
    if ocjena ==1:
        print('Nedovoljan.')
    elif ocjena > 5:
        print('Neispravan unos.')
        ocjena = int(input('Unesite ocjenu od 1 do 5: '))
    else:
        zbroj += ocjena

prosjek = zbroj/n
print('Prosjek ocjena je : ',prosjek)
















