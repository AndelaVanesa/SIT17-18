#Anđela Vanesa Tuta , 7.12.2017.
#Vjezba 7, zadatak 2

k = int(input('Unesite k: '))

i = 2
j = 0
while j<k:
    if i%3==0 or i%5==0:
        j+=1
        i+=2
        print(i,end='')
    else:
        i+=2
