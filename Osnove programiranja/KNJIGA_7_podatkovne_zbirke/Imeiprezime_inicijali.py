
def inicijali(s):
    m = s.index(' ')
    return s[0] + '. ' + s[m + 1] + '.'

def main():
    s = input('Ime i prezime: ')
    print(inicijali(s))

main()