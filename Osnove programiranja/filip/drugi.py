n = int(input('Unesite n: '))
if n == 0:
    n = int(input('n mora biti različit od 0. Ponovite unos: '))

djelitelji = []
for i in  range (-n, n+1):
    if i < 0 and i % 2 != 0 and n % i == 0:
        djelitelji.append(str(i))
    elif i > 0 and i % 2 == 0 and n % i == 0:
        djelitelji.append(str(i))

print(djelitelji)