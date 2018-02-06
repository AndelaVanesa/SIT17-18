#Zbrajamo sve ele u listi sa funkcijom



def zbr(lista):
    zbroj=0
    for i in lista: #Zbrajamo sve brojeve u listi
        zbroj+=i
    print(zbroj)
        
    return zbroj




def main():
    lista=[]
    for i in range(3):    #Unosimo 3 broja koja se dodaju u praznu listu
        n=int(input("br: "))
        lista.append(n)
        

    zbr(lista)


    
main()
   
        









