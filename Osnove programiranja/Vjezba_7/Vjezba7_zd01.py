#Anđela Vanesa Tuta , 7.12.2017.
#Učitava a koji je stranica kvadrata
#treba izračunati površinu kvadrata i dijagonalu


from math import sqrt
a = float(input('Unesi stranicu a:'))
p = a**2
d = a*sqrt(2)
print('Površina je',p,'a dijagonala', d)