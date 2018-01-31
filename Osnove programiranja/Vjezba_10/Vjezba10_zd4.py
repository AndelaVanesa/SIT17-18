#Anđela Vanesa Tuta, 20.1.2017
#Vjezba 10 zd 4


data=open("ulaz4.txt","r")
data_izlaz=open("izlaz4.txt","w")


lista_str = data.readlines()

for i in range(len(lista_str)):
    linija=lista_str[i].split()
    if linija[1] == "+":
        temp = float(linija[0])+float(linija[2])
    elif linija[1] == "-":
        temp = float(linija[0])-float(linija[2])
    elif linija[1] == "*":
        temp = float(linija[0])*float(linija[2])
    elif linija[1] == "/":
        temp = float(linija[0])/float(linija[2])


    data_izlaz.write(str(temp)+"\n")

        
   

    
    





data.close()
data_izlaz.close()


