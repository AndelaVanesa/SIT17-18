
m = int(input('Unesite m: '))
if m == 0:
    m = int(input('m mora biti različit od 0. Ponovite unos: '))
s = 0

for i in range (1,m):
    s += i/(i+1)
print('{:.2f}'.format(s))
