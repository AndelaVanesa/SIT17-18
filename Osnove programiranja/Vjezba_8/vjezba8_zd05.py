#Anđela Vanesa Tuta, 21.12.2017.
#Vježba 8, zadatak 5

def unos_int():
    n = input('Unesite cijeli broj: ')
    n = float(n)
    n = round(n)
    n = int(n)
    return n

def prost(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True

def main():
    print(prost(unos_int()))

    return

main()
