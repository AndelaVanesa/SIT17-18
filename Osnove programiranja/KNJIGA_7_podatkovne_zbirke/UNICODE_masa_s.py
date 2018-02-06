def UNICODEmasa(s):
    m=0
    for i in range(len(s)):
        m+=ord(s[i])
    return m

def main():
    s = input("Riječ: ")
    print(UNICODEmasa(s))

main()