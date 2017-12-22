#Andela Vanesa Tuta, 23.11.2017.
#Vjezba 5, zadatak 3

m = int(input('Unesite prirodan broj m veći od 0: '))
n = int(input('Unesite prirodan proj n veći od 0: '))

if m > 0 and n > 0 :
    lista_nzd = []
    for i in range (1,m+1 or n+1):
        if m%i==0 and n%i==0:
            lista_nzd.append(i)
    print('Najveći zajednički djeljitelj brojeva',m,'i',n,'je',max(lista_nzd),'.')


else:
    print('Uneseni broj manji je od 0.')