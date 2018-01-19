

m = int(input('Unesite m: '))
n = int(input('Unesite n: '))

s = 0
if n != 0 and m != 0:
    for i in range(1, m + 1):
        s = s + i / n
    print(s)
else:
    if m == 0:
        m = int(input('Broj mora biti različit od 0. Unesite m: '))
    if n == 0:
        n = int(input('Broj mora biti različit od 0. Unesite n: '))
    for i in range(1, m + 1):
        s = s + i / n
    print(s)



