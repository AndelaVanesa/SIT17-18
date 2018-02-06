ulaz = open('ulaz.txt', 'r')
izlaz = open('izlaz.txt', 'w')
lista = []
lista = ulaz.readlines()

print(lista)

for i in range(len(lista)):
    lista[i] = lista[i].split()

print(lista)

for i in range(len(lista)):
    lista[i] = lista[i][1], lista[i][0]

print(lista)

lista.sort(key=lambda i: i[1])

print(lista)

for i in range(len(lista)):
    izlaz.write('{}. {} {}\n'.format(i+1, lista[i][0], lista[i][1]))

ulaz.close()
izlaz.close()