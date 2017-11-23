#Andela Vanesa Tuta, 16.11.2017.
#Vjezba 4, zadatak 8

broj = int(input('Unesite cijeli broj veći od 1:'))

if n > 1:
    lista_p = []
    lista_n = []
    for i in range(1, n+1):
        if i%2 == 0:
            lista_p.append(i)
        else:
            lista_n.append(i)
    print(lista_p)
    print(lista_n)
    liste = lista_p + lista_n
    print(liste)
    liste.sort()
    print(liste)
else:
    print('Broj nije veći od 1.')