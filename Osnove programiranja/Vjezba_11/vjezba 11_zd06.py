from turtle import *

reset()
speed(0)

start = 300

for i in range(10):
    pu()
    goto(0,-start)
    pd()
    r=1.0-i*0.05
    g=1.0-i*0.05
    b=1.0-i*0.05
    fillcolor(r,g,b)
    begin_fill()
    circle(start)
    end_fill()
    start*= 0.9

mainloop()
