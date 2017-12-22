#Andela Vanesa Tuta, 23.11.2017.
#Vjezba 5, zadatak 1


#Ispis prvih n prirodnih brojeva
n = int(input('Unesite prirodan broj: '))
print('a) Prvih n prirodnih brojeva: ', end=' ')
for i in range(n) :
    print(i+1, end=' ')

#while petlja,
#iterator "i" definiran i nakon što for petlja završi s izvršavanjem
#reset
'''
i=1

while i<=n:
   print(i, end=' ')
   i +=1
'''
#Ispis prvih n neparnih prirodnih brojeva

print('b) Prvih n neparnih prirodnih brojeva: ',end=' ')
for i in range(n) :
    print(2*i+1, end=' ')

#Ispis vrijednosti n faktorijela
faktorijele = 1

print('c) n-faktorijela: ', end=' ')
for i in range(1, n+1):
    faktorijele *= i
print(faktorijele)

#Ispis svih parnih i neparnih manjih od n

if n%2 == 1 :
    for i in range (1,n+1) :
        if i%2 : print (i, end= ' ')
else :
    for i in range (1,int(n/2 + 1)) :
        print(2*i, end= ' ')


