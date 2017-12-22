#Andela Vanesa Tuta, 23.11.2017.
#Vjezba 5, zadatak 5

niz = input('Unesite niz znakova: ')

i = 0
while 1 < len(niz) :
    if i < len(niz)-1 :
        if niz[i:i+2].lower() == 'lj' or niz[i:i+2].lower() == 'nj' or niz[i:i+2].lower() == 'dž' :
            print(niz[i:i+2])
            i += 2
        elif niz[i].isalpha() :
            print(niz[i])
            i += 1
        else :
            i += 1
    else :
        if niz[i].isalpha() :
            print(niz[i])
            i += 1
