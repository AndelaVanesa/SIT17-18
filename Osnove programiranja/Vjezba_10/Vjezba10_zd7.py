#Anđela Vanesa Tuta, 20.1.2018
#Vjezba 10 zd 7

fin = open("ulaz7.txt", "r")
fout = open("izlaz7.txt", "w")
lista1 = fin.read().replace(",",".").split()
fin.close()
lista2 = list()

for i in lista1:
    while(i):
        try:
            if i[0] == "0":
                raise ValueError
            lista2.append(str(int(float(i))))
            break
        except ValueError:
            if (len(i) > 1):
                i = i[1:]
            else:
                break

lista2.sort()
str1 = ", ".join(lista2)
fout.write(str1)
fout.close()
