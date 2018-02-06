
def main():
    s = input('Riječ: ')
    st = ' '
    for i in range(0, len(s), 2):
        st += s[i] + ' '
    print(st)
main()