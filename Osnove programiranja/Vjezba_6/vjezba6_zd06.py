#Anđela Vanesa Tuta, 30.11.2017.
#Vjezba 6, zadatak 6

niz = 'abcd'

for i in niz:
    for j in niz:
        for k in niz:
            for l in niz:
                if i != j and i != k and j != l and i != l and j != k and j != l and k != l:
                    print((i+j+k+l), end = '\n')
