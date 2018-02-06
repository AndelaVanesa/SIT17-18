
def umetniZnak(s, n, z):
    return s[:n] + z + s[n:]

def main():
    s = input('Riječ: ')
    z = input('Znak: ')
    for i in range(len(s)+1):
        print(umetniZnak(s, i, z))

main()