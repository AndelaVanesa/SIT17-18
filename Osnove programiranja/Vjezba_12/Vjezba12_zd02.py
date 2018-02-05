#Anđela Vanesa Tuta
#Vježba 12, zadatak 2

def samoglasnici(s):
    if s in 'aeiouAEIOU':
        return True
    else:
        return False

def main():
    s = str(input('Unesite str:'))
    br = 0
    for i in range(len(s)):
        if samoglasnici(s[i]) == True:
            br+=1

    pos = (br/(len(s))*100)

    print(br,pos)
main()


