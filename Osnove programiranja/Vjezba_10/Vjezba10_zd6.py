#Anđela Vanesa Tuta, 20.1.2018
#Vjezba 10 zd 6

fin = open("ulaz6.txt", "r")
fout = open("izlaz6.txt", "w")
list1 = list()
list1 = fin.readlines()
 
for i in range(len(list1)):
    list1[i]=list1[i].split()
 
for i in range(len(list1)):
    list1[i]=(float(list1[i][1])/float(list1[i][2])**2, list1[i][0])
 
list1.sort(reverse=True)
 
for i in list1:
    fout.write(i[1]+" {0:.2f}\n".format(i[0]))
