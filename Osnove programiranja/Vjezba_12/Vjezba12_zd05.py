
import random
from turtle import *


speed = 0

n = int(input('Unesite prirodni broj veći od 0 i manji od 50: '))

pu()
goto(-150,-100)
pd()



colormode(255)
for i in range(5):
    s = random.randint(0, 255)
    fillcolor(s, s, s)
    begin_fill()
    for j in range(3):
        fd(300-n*i)
        lt(120)
    end_fill()




mainloop()
