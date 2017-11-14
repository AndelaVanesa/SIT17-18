#Anđela Vanesa Tuta, 2.11.2017.
#Vježba2, zadatak 7




x = float(input('Unesi prvi broj: '))
y = float(input('Unesi drugi broj: '))
z = float(input('Unesi treći broj: '))
#višestruko pridruživanjwe
print('x= {}, y= {}, z= {}'.format(x, y, z))

# x = z
# y = x
# z = y

#bez višestrukog pridruživanja-> privremene varijable
x, y, z = z, x, y

print('x= {}, y= {}, z= {}'.format(x, y, z))