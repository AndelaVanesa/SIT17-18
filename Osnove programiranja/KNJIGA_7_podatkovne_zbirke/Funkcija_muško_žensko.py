
def zensko(s):
    a = 'Aa'
    if s[len(s)-1] in a:
        return True
    else:
        return False

def main():
    n = int(input('Koliko ima imena? '))
    m = z = 0
    for i in range(n):
        ime = input ('Unesi ime: ')
        if zensko(ime) :
            z += 1
        else:
            m += 1
    print('Muških: {}\nŽenskih : {}'.format(m ,z))

main()