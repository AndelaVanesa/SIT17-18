#Andela Vanesa Tuta, 25.1.2018.
#Vjezba 11, zadatak 5


from turtle import *


n = int(input('Unesite broj vrhova n-terokuta: '))


reset()
speed(0)

if n > 2:
    pu()
    goto(0,-200)
    pd()
    fillcolor('red')
    begin_fill()
    circle(200,steps= n)
    end_fill()