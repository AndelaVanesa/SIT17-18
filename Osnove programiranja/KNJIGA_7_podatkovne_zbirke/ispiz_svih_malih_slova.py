
def malo(s):
    if s>= 'a' and s<= 'z':
        return True
    else:
        return False
def malaSlova(s):
    st = ''
    for i in range(len(s)):
        if malo(s[i]):
            st += s[i]
    return st

def main():
    s = input('Riječ: ')
    print(malaSlova(s))

main()