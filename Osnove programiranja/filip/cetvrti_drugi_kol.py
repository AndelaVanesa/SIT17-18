import math

def udaljenost_od_ishodista(T):
   d = math.sqrt(x ** 2 + y ** 2)
   return d

def main():
    global x
    global y
    x = int(input('Unesite x: '))
    y = int(input('Unesite y: '))
    T = (x, y)
    print('Udaljenost od ishodišta je za {} jediničnih dužina.'.format(udaljenost_od_ishodista(T)))

main()