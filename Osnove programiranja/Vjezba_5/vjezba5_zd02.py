#Andela Vanesa Tuta, 23.11.2017.
#Vjezba 5, zadatak 2

n = int(input('Unesite prirodan broj veći od 0: '))
brojac = 0

if n<1 :
    print('Unos mora biti veći od 0.')
else:
    for i in range(1, n+1) :
        if n%i == 0 :
            print(i)
            brojac += 1
    if brojac == 1 :
        print('Broj 1 nije ni prost ni složen.')
    elif brojac == 2 :
        print('Broj',n,' je prost broj.')
    else :
        print('Broj',n,'je složen i ima',brojač,'djeljitelja.')

