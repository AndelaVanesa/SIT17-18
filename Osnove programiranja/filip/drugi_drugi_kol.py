def interpunkcija(s):
    t = 0
    zar = 0
    dvo = 0
    toz = 0
    znakovi = '.,:;'
    for i in s:
        if i == '.':
            t += 1

        elif i == '.':
            zar += 1

        elif i == ':':
            dvo += 1

        elif i == ';':
            toz += 1
    a = ('točki ima, ', t, 'zareza ima ', zar, 'dvotočki ima: ', dvo, ' točka zarez ima: ', toz)
    return (a)


def main():
    s = input('upis: ')
    print(interpunkcija(s))


main()

