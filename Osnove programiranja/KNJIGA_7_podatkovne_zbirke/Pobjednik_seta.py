def pobjednikSeta(s):
    a=b=0
    for i in range(len(s)):
        if s[i]=="A":
            a+=1
        else:
            b+=1
    if a > b:
        return "A"
    else:
        return "B"

def main():
    n = int(input("Broj setova: "))
    a=b=0
    for i in range(n):
        s=input("Rezultat seta: ")
        if pobjednikSeta(s)=="A":
            a+=1
        else:
            b+=1
    print("{} : {}".format(a, b))

main()