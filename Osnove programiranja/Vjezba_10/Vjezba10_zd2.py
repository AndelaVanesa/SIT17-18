#Anđela Vanesa Tuta, 20.1.2017
#Vjezba 10 zd 2


data=open("ulaz2.txt","r")


s = data.read()


izlaz = str()

for i in s:
    brojac = 0
    for j in s:
        if j ==1:
            brojac+=1
    if brojac > 1:
        if not i in izlaz:
            izlaz+=i

if len(izlaz)>0:
    print(izlaz)
else:
    print("Niti jedan znak se ne ponavlja.")


    
    





data.close()


