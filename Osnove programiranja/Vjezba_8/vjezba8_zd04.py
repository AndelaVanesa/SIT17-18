#Anđela Vanesa Tuta, 21.12.2017.
#Vjezba 8, zadatak 4

def binarno_pretrazivanje(lista,s):

    l = len(lista)
    if l == 0:
        return False
    elif s == lista[l//2]: return True
    elif s<lista[l//2]:
        return binarno_pretrazivanje(lista[0:l//2],s)
    else:
        return binarno_pretrazivanje(lista[l//2+1:l],s)

def main ():
    lista=[1,6,7,8,9,4,5,3]
    lista.sort()
    x=binarno_pretrazivanje(lista,7)
    print(x)
main()
