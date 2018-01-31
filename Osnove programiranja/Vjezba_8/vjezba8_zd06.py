#Anđela Vanesa Tuta, 21.12.2017.
#Vjezba 8, zadatak 6

def unos_u_listu(lista):
    lista = []
    x = input('Unesite broj(ili slovo za prekid): ')

    if x.isdigit():
        lista.append(float(x))
        return lista
    else:
        return lista

def max_element(lista):

    if len(lista)== 0:
        return
    max_el = lista[0]

    for i in lista:
        if i>max_el:
            max_el =i
    return max_el
def main():
    lista = []
    lista_nova = []
    while len(lista_nova) == len(lista)

print('Maksimalni element liste je',max_element(lista))

    return


main()


    return
