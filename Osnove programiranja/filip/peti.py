niz_1 = str(input('Unesite niz znakova: '))
niz_2 = niz_1.swapcase()
tocke = niz_1.count('.')
zarezi = niz_1.count(',')
razmaci = niz_1.count(' ')
print(niz_2)
print('Vaš niz {} ima {} točkaka, {} zareza i {} razmaka.'.format(niz_1, tocke, zarezi, razmaci))