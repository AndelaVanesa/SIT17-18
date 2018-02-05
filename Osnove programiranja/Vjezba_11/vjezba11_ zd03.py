#Andela Vanesa Tuta, 25.1.2018.
#Vjezba 11, zadatak 3


from turtle import *

n = int(input('Unesite broj vrhova n-terokuta: '))

reset()
if n > 2:

    for i in range (n):
        write(str(i+1),align='right', font =('Arial',11,'bold'))
        fd(100)
        lt(360/n)

else:
    print('Pogrešan unos.')
mainloop()
'''
if n > 2:
    pu()
    goto(0,-200)
    pd()
    circle(200,steps= n)
'''