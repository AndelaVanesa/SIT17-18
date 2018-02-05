#Andela Vanesa Tuta, 25.1.2018.
#Vjezba 11, zadatak 1

from turtle import *

reset()

pu()

goto(-200,-200)

pd()

vrhovi = 'ABCD'

for i in vrhovi:
    write(i)
    fd(400)
    lt(90)

goto(200,200)
bk(400)
goto(200,-200)
pu()
mainloop()




