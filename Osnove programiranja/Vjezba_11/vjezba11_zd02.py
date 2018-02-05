#Andela Vanesa Tuta, 25.1.2018.
#Vjezba 11, zadatak 2 GREŠKA

def kvadrat (duljina):

    pu()

    goto(-duljina//2, -duljina//2)

    pd()

    for i in range(4):
        fd(duljina)
        lt(90)
        return
    mainloop()

def main():
    reset()
    n = int(input('Unesi duljinu stranice kvadrata: '))
    if n > 0:
        kvadrat(n)
    else:
        print('Pogrešan unos. DUljina stranice mora biti veća od 0.')
    kvadrat(n)
    return
