#Anđela Vanesa Tuta, 20.1.2017
#Vjezba 10 zd 1


data=open("ulaz1.txt","r")


s = data.read()

izlaz = str()



for znak in s:
    if str.isalpha(znak):
        izlaz+=znak

print(izlaz)

data.close()


