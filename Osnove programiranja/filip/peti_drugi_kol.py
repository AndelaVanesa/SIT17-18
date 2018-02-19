from turtle import *

reset()
speed(0)
colormode(255)

n = int(input('Unesi n (0<n<300): '))

pu()
goto(0, -n)
pd()

circle(n)
end_fill()
fillcolor('black')
begin_fill()
circle(200, steps=5)
end_fill()

mainloop()