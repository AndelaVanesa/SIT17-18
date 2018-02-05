
def povrsina(x1, y1, x2, y2, x3, y3):
    P = (1/2)*(abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
    if P == 0:
        print('Zadane točke ne tvore trokut.')
    else:
        return P

def main():

    x1 = int(input('Unesite x1:'))
    y1 = int(input('Unesite y1:'))
    x2 = int(input('Unesite x2:'))
    y2 = int(input('Uneisite y2:'))
    x3 = int(input('Unesite x3:'))
    y3 = int(input('Unesite y3:'))

    T_1 = (x1,y1)
    T_2 = (x2,y2)
    T_3 = (x3,y3)
    print(T_1, T_2, T_3)
    P = povrsina(x1, y1, x2, y2, x3, y3)
    print('Površina trokuta iznosi {} cm^2'.format(P))
main()
