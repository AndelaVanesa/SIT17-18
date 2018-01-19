#Anđela Vanesa Tuta , 7.12.2017.


m = int(input('Unesite m: '))
n = int(input('Unesite n: '))
umnozak_lista = []
umnozak = 1
if m < n:
    for i in range (m+1,n):
        umnozak_lista.append(i)
        for x in umnozak_lista:
                umnozak *= x
                print(umnozak)
else:
    print('m ({}) je veći ili jednak 0.'.format(m))



