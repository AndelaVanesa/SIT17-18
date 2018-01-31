#Anđela Vanesa Tuta, 20.1.2018
#Vjezba 10 zd 5

def broji_znamenke(znamenka, string):
    counter = 0
    for i in string:
        if (str(i) == str(znamenka)):
            counter += 1
    return counter

# main


fin = open("ulaz5.txt", "r")
fout = open("izlaz5.txt", "w")

str1 = fin.read()

for i in str1:
    if not i.isdigit():
        str1 = str1.replace(i, "")

for i in range(10):
    counter = broji_znamenke(i, str1)
    if counter > 0:
        fout.write("# {} - {:0.2f}\n".format(i, float(counter)/float(len(str1))))
