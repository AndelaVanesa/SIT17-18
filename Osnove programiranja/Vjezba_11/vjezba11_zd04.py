#Andela Vanesa Tuta, 25.1.2018
#Vjezba 11 zd 3

from turtle import *

n=int(input("Unesite br vrhova n-terokuta: "))



reset()

if n>2:
    pu()
    goto(0, -200)
    pd()
    circle(200)
    circle(200, steps=n)
    
else:
    print("Greška!")
    
