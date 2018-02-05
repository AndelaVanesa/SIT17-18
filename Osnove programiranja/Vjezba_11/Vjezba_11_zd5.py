#Stipe Bačić 25.1.2018
#Vjezba 11 zd 5

from turtle import *

n=int(input("Unesite br vrhova n-terokuta: "))



reset()

if n>2:
    pu()
    goto(0, -200)
    pd()
    fillcolor("red")
    begin_fill()
    circle(200)
    end_fill()
    fillcolor("blue")
    begin_fill()
    circle(200, steps=n)
    end_fill()
    fillcolor("green")
    begin_fill()
    circle(100)
    end_fill()
    
else:
    print("Greška!")
    
