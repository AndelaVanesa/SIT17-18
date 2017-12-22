#Andela Vanesa Tuta, 23.11.2017.
#Vjezba 5, zadatak 10

n= int(input('Unesite prirodan broj: '))

if n <= 0:
    print('Greška.')
else:
    while n > 0 :
        niz = str(n)

        pronadjen = True


        for i in range(len(niz)//2):
            if niz[i] != niz[(len(niz)-1)-i] :
                pronadjen = False
        if pronadjen :
             print(n)
             break
        else:
            n -= 1


