
n = int(input('Unesite n: '))


if n != 0:
    for i in range (-n,  n+1):
        if i == 0:
            continue
        if n % i == 0 and i % 2 == 0:
            print(i, end= ' ')
else:
    n = int(input('Broj mora biti različit od 0. Ponovite unos: '))
    for i in range (-n,  n+1):
        if i == 0:
            continue
        if n % i == 0 and i % 2 == 0:
            print(i, end= ' ')
