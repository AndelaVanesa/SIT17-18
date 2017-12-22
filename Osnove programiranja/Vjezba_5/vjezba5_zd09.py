#Anđela Vanesa Tuta, 23.11.2017.
#Vjezba 5, zadatak 9

m = int(input('Unesite prvi prirodni broj: '))
n = int(input('Unesite drugi prirodni broj: '))

brojac = 0
if m < n:
    for i in range(m + 1, n):
        broj = [int(x) for x in str(i)]
        zbroj = sum(broj)
        if zbroj == 10:
            print(i)
            brojac +=1

    if broj == 0:
        print('U rasponu od {} do {} nema znamenaka kojima je zbroj jednak 10.'.format(m,n))
else:
    for i in range(n + 1, m):
        broj = [int(x) for x in str(i)]
        zbroj = sum(broj)
        if zbroj == 10:
            print(i)
            brojac += 1
    if brojac == 0:
        print('U rasponu od {} do {} nema brojeva kojima je zbroj znamenaka jednak 10.'.format(n ,m))