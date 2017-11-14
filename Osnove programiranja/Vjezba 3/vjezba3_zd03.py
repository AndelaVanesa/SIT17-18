#Anđela Vanesa Tuta, 10.11.2017.
#Vjezba 3, zadatak 3

# korisnik unosi 2 cijela broja i računsku operaciju

a=int(input('Unesite prvi broj:'))
b=int(input('Unesite drugi broj:'))

operacija = input('Unesite računsku operaciju (+,-,*,/)')

if operacija == '+':
    print('Zbroj je = ', a+b)
elif operacija == '-':
    print('Razlika je = ', a-b)
elif operacija == *:
    print('Umnožak je = ', a*b)
elif operacija == '/':
    print('Količnik je = ' ,a/b)
else:
print('Niste unijeli ispravnu računski operaciju.')