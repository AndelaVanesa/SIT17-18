
niz_1 = str(input('Unesite niz znakova: '))
niz_2 = niz_1.swapcase()
tocke = niz_1.count('.')
zarezi = niz_1.count(',')
razmaci = niz_1.count(' ')
print(niz_2)
print(f'Vaš niz {niz_1} ima {tocke} točku/ke,aka, {zarezi} zarez/a i {razmaci} razmak/a.')
