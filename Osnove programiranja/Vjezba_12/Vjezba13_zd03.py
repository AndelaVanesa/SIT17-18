


ulaz = open('ulaz_1.txt','r')
izlaz = open('izaz.txt','w')

#readlines -> svaku liniju teksta u txt datoteci stavlja u listu(Svaka linija je element u listi)
#readline -> 1 liniju pretvara u element liste
#read-> učitava cijelu datoteku i ispisuje je kao string

lista = []
lista = ulaz.readlines()
print(lista)
for i in range(len(lista)):
    lista[i] = lista[i].split()

lista.sort(reverse=True)
print(lista)
for i in range(len(lista)):
    izlaz.write('{}. {} {}\n'.format(i+1, lista[i][0], lista[i][1]))
ulaz.close()
izlaz.close()