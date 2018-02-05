


from turtle import *
import random


n = textinput('Unos', 'Unesite broj točaka i veličinu točke (odvojeno zarezom)').split(',')

velicina = int(n[1])
broj_tocaka = int(n[0])

colormode(255)
for i in range(broj_tocaka):
    pu()
    x = random.randint(-300 ,300)
    y = random.randint(-300 ,300)
    goto(x, y)
    pd()

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)

    dot(n[1])
    color = ('red')
    pu()
    sety(y-velicina-10)
    pd()
    write('('+str(x)+','+str(y)+')', align='center')
mainloop()
