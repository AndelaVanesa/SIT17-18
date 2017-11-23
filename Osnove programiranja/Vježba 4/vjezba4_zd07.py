#Anđela Vanesa Tuta, 16.11.2017.
#Vježba 4, zadatak 7

n = int(input('Unesite cijeli broj veći od jedan: '))

if n>1:
    lista = list(range(1,n+1))
    lista.reverse()
    print(lista)
    lista_2 = list(range(2*n,0,-2))
    lista_2.reverse()
    print(lista_2)
else:
    print('Broj je manji od 1.')
